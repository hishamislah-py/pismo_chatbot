---
ku_id: KU-EVT-client-webhooks-part-04
title: Client webhooks (part 4 of 14)
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/client-webhooks.md
  sha256: cd35b3bad1d1b22bcca9904923038c09b3581f0196a1afc2f4a7a436effd79f4
  url: https://developers.pismo.io/pismo-docs/docs/client-webhooks
  role: primary_guide
  updated_at: '2026-09-18T17:12:01.000Z'
operations: []
related_kus:
- KU-CC-processing-codes
- KU-ERR-validation-codes-for-authorization-events-part-01
- KU-ERR-validation-codes-for-authorization-events-part-02
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 4 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-04` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> target="_blank" rel="noopener noreferrer">
>                                                              Processing codes and transaction types

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 1241–1649 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=1240-1649 -->
                                                                                                     <br>For more information, refer to the <a href="https://developers.pismo.io/pismo-docs/docs/cc-manage-processing-codes-and-transaction-types"
                                                             target="_blank" rel="noopener noreferrer">
                                                             Processing codes and transaction types
                                                          </a> guide.</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>currency</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Transaction country currency code - ISO 4217. For example,
                                                                                                                                                                                                          <br><code>840</code> (US)
                                                                                                                                                                                                          <br><code>986</code> (Brazil)
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>payment_card_brand</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Transaction brand -
                                                                                                                                                                                                          <code>Visa</code> or
                                                                                                                                                                                                          <code>Mastercard</code>.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>merchant_id_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Merchant code as registered at the payments network database (Visa/Mastercard)</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>merchant_name</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Merchant name as registered at the payments network database (Visa/Mastercard)</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>merchant_city</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Merchant city as registered at the payments network database (Visa/Mastercard)</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>merchant_state_or_country_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Merchant country code outside USA (OR) Merchant state code from the USA (OR) Canadian province code from Canada.
                                                                                                                                                                                                          <br>NOTE: Canadian merchants can either be represented through the province code or the canadian country code.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>merchant_terminal_id</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Terminal ID at acquirer database</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>atc_chip</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Application Transaction Counter acquired from ISO8583 formatted payments network message</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>atc_database</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Application Transaction Counter acquired from authorization platform database. Comma-separated array of numbers, for example "[1, 3, 6]".</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cvv_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>CVV data</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>entry_mode</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Method used for PAN entry to initiate a transaction and the PIN entry capabilities. This field is required and must have 3 or 4 digits.
                                                                                                                                                                                                          <br>For example, try
                                                                                                                                                                                                          <code>901</code> or
                                                                                                                                                                                                          <code>9010</code> for magnetic stripe transaction simulation.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>mcc</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Merchant category codes payments network.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>card_type</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Transaction cardholder card type enum:
                                                                                                                                                                                                          <br>
                                                                                                                                                                                                          <code>PLASTIC</code>
                                                                                                                                                                                                          <br>
                                                                                                                                                                                                          <code>VIRTUAL</code>
                                                                                                                                                                                                          <br>
                                                                                                                                                                                                          <code>TEMPORARY</code>
                                                                                                                                                                                                          <br>
                                                                                                                                                                                                          <code>RECURRING</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>country_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Card issuer location's country code - ISO 3166-1</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_validation</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>Is chip valid flag</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>postal_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Card issuer location's postal code</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_cryptogram_information_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Relevant information data from cardholder chip</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_transaction_date</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Transaction date from cardholder chip. Format: <code>yymmdd.</code></td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_transaction_type</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Specific transaction type</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_amount_authorized</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Amount authorized for cardholder. Format: 000000000010)</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_transaction_currency_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Specific given currency code</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_application_interchange_profile</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Application interchange profile information</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_terminal_country_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Terminal country code from payment network.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_cardholder_verification_method</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Cardholder authorization verification method</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_terminal_capabilities</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Capability code given by POS. Each code has the list of capabilities classified.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_amount_other</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | niull</td>
                                                                                                                                                                                                          <td>If there is no cash back amount, the value of 9F03 is zero. 9F03 may be absent, or present with a zero value.
                                                                                                                                                                                                          <br>If there is a cash back amount, presence is mandatory.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>chip_application_transaction_counter</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>DE 120 (record data) contains Application Transaction Counter file data when DE 101 (file name) contains MCC109</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cardholder_postal_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Cardholder postal code</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>transaction_type</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string| null</td>
                                                                                                                                                                                                          <td>Processing code that describes the transaction type being authorized.
                                                                                                                                                                                                          <br>This processing code is the first 2 characters of the mapped code.
                                                                                                     <br><code>"00"</code> for purchases.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>nsu</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Authorization Network Settlement Utility (NSU) number which tracks the flow of funds between parties involved in a payment card transaction, including the bank, the merchant, and the card network.
                                                                                                                                                                                                          <br>Different payment card networks may have their own NSU systems (e.g., Visa - VisaNet, Mastercard - BankNet) or they may use a third party.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>retrieval_reference_number</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Merchant POS system generated number</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>authorization_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Authorization code</td>
                                                                                                                                                                                                          <td>Y <br> 6-character alphanumeric code. When the network provides an authorization code in the advice (e.g., STIP), the network-provided code is used. Otherwise, a code is generated by the issuer processor.</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>incoming_authorization_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Authorization code from card network</td>
                                                                                                                                                                                                          <td>C <br> Original authorization code received from the network. Only present when the network provides one (e.g., STIP advice scenarios). Empty when the authorization originated from the issuer.</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>response_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Network two digit response code. For example:
                                                                                                                                                                                                          <br><code>00</code> = approve
                                                                                                                                                                                                          <br><code>51</code> = insufficient funds
                                                                                                                                                                                                          <br><code>57</code> = card not active
                                                                                                                                                                                                          <br><code>96</code> = system failure, etc.
                                                                                                                                                                                                          <br>For more information, refer to
                                                                                                                                                                                                          <a href="https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events" target="_blank">Validation codes for authorization events</a>.
                                                                                                                                                                                                          <br>If
                                                                                                                                                                                                          <code>approve</code> =
                                                                                                                                                                                                          <code>false</code>, you can use this value to respond to the network.
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>terminal_capability</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Point-of-sale (POS) entry mode code</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>tvr</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Terminal verification results: serves as notification of bit validation errors detected in the TVR within the issuer application data during M/Chip Cryptogram Validation processing.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cvr</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string | null</td>
                                                                                                                                                                                                          <td>Card verification results: serves as notification of bit validation errors detected in the CVR within the issuer application data during M/Chip Cryptogram Validation processing.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>number_of_installments</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>int</td>
                                                                                                                                                                                                          <td>Authorization's number of installments</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>network_score</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>number</td>
                                                                                                                                                                                                          <td>Payment network score: empty field when no information is present.</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>pos_postal_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Terminal machine authorizer postal code</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>acquirer_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Authorizer acquirer code</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>denial_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Code that identifies reason the transaction was denied</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>financial_network_code</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Financial code from card network</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>banknet_reference_number</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>string</td>
                                                                                                                                                                                                          <td>Authorization banknet reference number</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr style="background-color: beige;">
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>original_network_data</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>object</td>
                                                                                                                                                                                                          <td>Raw ISO-8583 message without sensitive fields.</td>
                                                                                                                                                                                                          <td>Y</td>
                                                                                                                                                                                                          </tr>
                                                                                                                                                                                                          <tr>
                                                                                                                                                                                                          <td style="padding-left: 30px;">
                                                                                                                                                                                                          <code>cvv_presence</code>
                                                                                                                                                                                                          </td>
                                                                                                                                                                                                          <td>bool</td>
                                                                                                                                                                                                          <td>Is CVV data present flag</td>
                                                                                                                                                                                                          <td>N</td>
                                                                                                                                                                                                          </tr>
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 1241–1649 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- `KU-CC-processing-codes` — Control Center processing codes, transaction types and general ledger accounts
- `KU-ERR-validation-codes-for-authorization-events-part-01` — Validation codes for authorization events (part 1 of 2)
- `KU-ERR-validation-codes-for-authorization-events-part-02` — Validation codes for authorization events (part 2 of 2)
