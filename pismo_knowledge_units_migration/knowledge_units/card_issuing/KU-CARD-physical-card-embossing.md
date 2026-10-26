---
ku_id: KU-CARD-physical-card-embossing
title: Physical card embossing
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/physical-card-embossing.md
  sha256: 7521b7feeb28d303847d1fb7a1da7569268c268f612ae72ec9360672c706604b
  url: https://developers.pismo.io/pismo-docs/docs/physical-card-embossing
  role: primary_guide
  updated_at: '2026-07-21T18:09:22.000Z'
operations:
- create-bulk
- delete-cards-embossing
- get-embossing-configurations-info
- get-embossing-download-file
- get-embossing-file-info
- get-embossing-info
- get-noname-embossing-info
- patch-embossing-group
- patch-noname-embossing-group
- patch-v2-card
- post-acquisitions-v3-s2s-applications
- post-generate-embossing
- post-v1-card-reissue
- post-v2-card
- put-cards-embossing
- start-bulk
- start-embossing
- start-reembossing
related_kus:
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--embossing
- KU-API-card-issuing-cards--embossing-data
- KU-API-card-issuing-cards--embossing-encrypted
- KU-API-card-issuing-cards--noname
- KU-API-core-platform-accounts--accounts
- KU-AUTH-pismo-platform-security-guide
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-other-domains
- KU-EVT-data-events-concepts
- KU-RPT-scheduled-reports
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Physical card embossing

**KU ID:** `KU-CARD-physical-card-embossing` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/physical-card-embossing.md`:

> You can use the Pismo platform to issue physical cards using your chosen [embossing](https://www.investopedia.com/terms/e/embossed-card.asp) provider or **providers**. After setting up your program, you need to meet with your Pismo representative to configure your embossing **provider(s)** and schedule.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/physical-card-embossing.md`: Physical card embossing; Embossers; Embossing layouts; Track 1; Track 2; Track 1; Track 2; Embossing flows; Step 1—Create physical card; Step 2—Define/mark card for embossing; Step 3—Retrieve embossing configurations; Step 4—Start embossing process; Step 5—Retrieve generated file details; Step 6—Download file; Step 1—Create noname card; Step 2—Start noname bulk process; Step 3—Retrieve embossing configurations; Step 4—Start embossing process; Step 5—Retrieve generated file details; Step 6—Download file; Working with more than one embosser; Embossing rules; Passwords; On demand embossing - override card password updated requirement; Issuer Public Key (IPK) certificate; Pretty Good Privacy (PGP) key encryption; Troubleshooting embossing errors; Embossing API endpoints; Embossing events

## Prerequisites and dependencies

- Prerequisites are described in `docs/card-issuing/physical-card-embossing.md` section "On demand embossing - override card password updated requirement".
- Depends on 18 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/physical-card-embossing.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/physical-card-embossing · updatedAt: 2026-07-21T18:09:22.000Z

<!-- source:begin path=docs/card-issuing/physical-card-embossing.md part=0-end -->

# Physical card embossing

You can use the Pismo platform to issue physical cards using your chosen [embossing](https://www.investopedia.com/terms/e/embossed-card.asp) provider or **providers**. After setting up your program, you need to meet with your Pismo representative to configure your embossing **provider(s)** and schedule.

There are three types of physical (plastic/metal) card that most embossers can issue:

* **Mag stripe card**—Card data is stored in a magnetic strip. A customer swipes the card to use it. This type of card is easy to counterfeit, because the data in the strip is static.
* **Europay, Mastercard, and Visa (EMV) contact card**—Card data is stored in a chip. A customer dips (inserts) the card to use it. The cryptography in the chip creates tumbling security codes, making it much harder to counterfeit, but it costs more to issue.
* **Dual interface card**—Card data is stored in a chip. There is also an embedded antenna, so a customer can either dip or tap to use the card. This is the most convenient type of card for the customer, but it's the most expensive to issue.

The embossing process occurs daily according to your requested schedule, which can run at different times on different days. During an embossing run, Pismo submits all eligible cards and their required data via an encrypted file to the **embosser(s)** via Odette File Transfer Protocol (OFTP)  or Secure File Transfer Protocol (SFTP).

The following API endpoints allow you to view or revise your personalized embossing configuration information:

* [Get nominal card embossing information](https://developers.pismo.io/pismo-docs/reference/get-embossing-info)
* [Update nominal card embossing group](https://developers.pismo.io/pismo-docs/reference/patch-embossing-group)
* [Get noname card embossing information](https://developers.pismo.io/pismo-docs/reference/get-noname-embossing-info)
* [Update noname card embossing group](https://developers.pismo.io/pismo-docs/reference/patch-noname-embossing-group)

For nominal cards, a customer is designated the cardholder at card creation. Noname cards are batch-generated and not initially associated with customers, which occurs later.

> 🚧 Noname versus named cards
>
> The embossing layouts used for noname and named embossing processes are different. If you plan to use both noname and named cards, you need to set up layouts for both with your chosen embosser.

The printed name on cards is set when you [create an account](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications). After that, you can call the [Update card information](https://developers.pismo.io/pismo-docs/reference/patch-v2-card) endpoint to revise it.

# Embossers

The following are embossers Pismo currently work with:

* [JallCard](https://www.jallcard.com.br/empresa)
* [Gemalto (Thales)](https://www.thalesgroup.com/en/markets/digital-identity-and-security)
* Alterosa
* EM1
* [Idemia](https://www.idemia.com/)
* [Intelcav](https://cpcintelcav.com.br/)
* [Seshasai](https://seshaasai.com/)
* Valid
* [Manipal](https://manipalglobalprintsolutions.com/)
* Colorplast
* [G\&D](https://www.gi-de.com/en/)
* Nacion
* [Toppan](https://odoo.toppansecurity.com/)
* [CSP](https://www.rscustomproducts.com/category/certified-safety-professional_0)
* PlusTech
* Thomas Greg

If you have an embosser not listed here that you would like to work with, please let us know.

# Embossing layouts

The following are common card network Track 1 and Track 2 layouts for embossing. You need to work with your Pismo representative to configure your card's layouts.

<details>
  <summary style={{ fontSize: "20px" }}><b>Visa, Mastercard, and ELO</b></summary>

  ### Track 1

  * Max length = 79
  * Example: B5112586722254937^HOLDER/CARD               ^2312201000000000000000936000000?

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th>
          Data
        </th>

        <th>
          Length
        </th>

        <th>
          Value
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          Start sentinel
        </td>

        <td>
          1
        </td>

        <td>
          %
        </td>
      </tr>

      <tr>
        <td>
          Format code
        </td>

        <td>
          1
        </td>

        <td>
          B
        </td>
      </tr>

      <tr>
        <td>
          Primary Account Number (PAN)
        </td>

        <td>
          12-19
        </td>

        <td>
          0-9
        </td>
      </tr>

      <tr>
        <td>
          Separator
        </td>

        <td>
          1
        </td>

        <td>
          ^
        </td>
      </tr>

      <tr>
        <td>
          Cardholder/printed name
        </td>

        <td>
          2-26
        </td>

        <td>
          including separators , where appropriate, between surname, first name
        </td>
      </tr>

      <tr>
        <td>
          Separator
        </td>

        <td>
          1
        </td>

        <td>
          ^
        </td>
      </tr>

      <tr>
        <td>
          Expiration date
        </td>

        <td>
          4
        </td>

        <td>
          Format = YYMM
        </td>
      </tr>

      <tr>
        <td>
          Service code
        </td>

        <td>
          3
        </td>

        <td>
          0-9
          201 - default Pismo
          XXX - possibility of customization according to the issuer/program
        </td>
      </tr>

      <tr>
        <td>
          Discretionary data
        </td>

        <td>
          Balance of available digits
        </td>

        <td>
          Offset - default Pismo (length 15), but with the possibility of customization according to the issuer/program
          CVV - length 3
          Remaining, filled with 0 to complete the field size
        </td>
      </tr>

      <tr>
        <td>
          End sentinel
        </td>

        <td>
          1
        </td>

        <td>
          ?
        </td>
      </tr>
    </tbody>
  </Table>

  ### Track 2

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th>
          Data
        </th>

        <th>
          Length
        </th>

        <th>
          Value
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          Start sentinel
        </td>

        <td>
          1
        </td>

        <td>
          :
        </td>
      </tr>

      <tr>
        <td>
          Primary Account Number (PAN)
        </td>

        <td>
          12-19
        </td>

        <td>
          0-9
        </td>
      </tr>

      <tr>
        <td>
          Separator
        </td>

        <td>
          1
        </td>

        <td>
          \= or D
        </td>
      </tr>

      <tr>
        <td>
          Expiration date
        </td>

        <td>
          4
        </td>

        <td>
          Format = YYMM
        </td>
      </tr>

      <tr>
        <td>
          Service code
        </td>

        <td>
          3
        </td>

        <td>
          0-9
          201 - Pismo default
          XXX - Customization possible according to the issuer/program
        </td>
      </tr>

      <tr>
        <td>
          Discretionary data
        </td>

        <td>
          Balance of available digits
        </td>

        <td>
          Offset - Pismo default, length 5.
          But with the possibility of customization according to the issuer/program
          CVV - Length 3
          Remaining filled with 0 to complete the field size
        </td>
      </tr>

      <tr>
        <td>
          End sentinel
        </td>

        <td>
          1
        </td>

        <td>
          ? or F
        </td>
      </tr>
    </tbody>
  </Table>
</details>

<details>
  <summary style={{ fontSize: "20px" }}>
    <b>RuPay</b>
  </summary>

  ### Track 1

  * Maximum length = 79
  * **Example**: B3561580000186920^HOLDER/CARD               ^2807226673A000000000000        ?

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th>
          Data
        </th>

        <th>
          Length
        </th>

        <th>
          Value
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          Start sentinel
        </td>

        <td>
          1
        </td>

        <td>
          %
        </td>
      </tr>

      <tr>
        <td>
          Format code
        </td>

        <td>
          1
        </td>

        <td>
          B
        </td>
      </tr>

      <tr>
        <td>
          PAN
        </td>

        <td>
          12-19
        </td>

        <td>
          0-9
        </td>
      </tr>

      <tr>
        <td>
          Separator
        </td>

        <td>
          1
        </td>

        <td>
          ^
        </td>
      </tr>

      <tr>
        <td>
          Cardholder/printed name
        </td>

        <td>
          2-26
        </td>

        <td>
          Including separators , where appropriate, between surname, first name
        </td>
      </tr>

      <tr>
        <td>
          Separator
        </td>

        <td>
          1
        </td>

        <td>
          ^
        </td>
      </tr>

      <tr>
        <td>
          Expiration date
        </td>

        <td>
          4
        </td>

        <td>
          Format = YYMM
        </td>
      </tr>

      <tr>
        <td>
          Service code
        </td>

        <td>
          3
        </td>

        <td>
          0-9
          201 - default Pismo
          XXX - possibility of customization according to the issuer/program
        </td>
      </tr>

      <tr>
        <td>
          Card Verification Value (CVV)
        </td>

        <td>
          3
        </td>

        <td>
          0-9
        </td>
      </tr>

      <tr>
        <td>
          Aadhaar number (document number)
        </td>

        <td>
          13
        </td>

        <td>
          A, 0-9
        </td>
      </tr>

      <tr>
        <td>
          Discretionary data
        </td>

        <td>
          Balance of available digits
        </td>

        <td>
          Offset - default Pismo (length 15), but with the possibility of customization according to the issuer/program
          CVV - length 3
          Remaining, filled with 0 to complete the field size
        </td>
      </tr>

      <tr>
        <td>
          End sentinel
        </td>

        <td>
          1
        </td>

        <td />
      </tr>
    </tbody>
  </Table>

  ### Track 2

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th>
          Data
        </th>

        <th>
          Length
        </th>

        <th>
          Value
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          Start sentinel
        </td>

        <td>
          1
        </td>

        <td>
          :
        </td>
      </tr>

      <tr>
        <td>
          Primary Account Number (PAN)
        </td>

        <td>
          12-19
        </td>

        <td>
          0-9
        </td>
      </tr>

      <tr>
        <td>
          Separator
        </td>

        <td>
          1
        </td>

        <td>
          \= or D
        </td>
      </tr>

      <tr>
        <td>
          Expiration date
        </td>

        <td>
          4
        </td>

        <td>
          Format = YYMM
        </td>
      </tr>

      <tr>
        <td>
          Service code
        </td>

        <td>
          3
        </td>

        <td>
          0-9
          201 - default Pismo
          XXX - possibility of customization according to the issuer/program
        </td>
      </tr>

      <tr>
        <td>
          CVV
        </td>

        <td>
          3
        </td>

        <td>
          0-9
        </td>
      </tr>

      <tr>
        <td>
          Discretionary data
        </td>

        <td>
          Balance of available digits
        </td>

        <td>
          0
        </td>
      </tr>

      <tr>
        <td>
          End sentinel
        </td>

        <td>
          1
        </td>

        <td>
          ? or F
        </td>
      </tr>
    </tbody>
  </Table>
</details>

# Embossing flows

<details>
  <summary style={{ fontSize: "20px" }}><b>Nominal cards</b></summary>

  The following is the step-by-step guide to obtain a test embossing file in the EXT/HOMOLOG testing environment:

  ### Step 1—Create physical card

  Call the [Create card ](https://developers.pismo.io/pismo-docs/reference/post-v2-card)endpoint to create a physical card.

  As this is an asynchronous process, the following events are generated:

  * [Card created ](https://developers.pismo.io/events/docs/cards-create-1)
  * [Card can be added to next scheduled embossing ](https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1)

  ### Step 2—Define/mark card for embossing

  Call the [Add card to next scheduled embossing ](https://developers.pismo.io/pismo-docs/reference/put-cards-embossing) endpoint to define/mark the card for embossing.

  You can call the [Delete card from next scheduled embossing](https://developers.pismo.io/pismo-docs/reference/delete-cards-embossing) endpoint to remove the card from the embossing queue.

  ### Step 3—Retrieve embossing configurations

  Call the [Get org embosser info ](https://developers.pismo.io/pismo-docs/reference/get-embossing-configurations-info)endpoint to retrieve the embossing configurations.

  ### Step 4—Start embossing process

  Call the [Start card embossing](https://developers.pismo.io/pismo-docs/reference/start-embossing) endpoint to begin the embossing process

  The following events are generated:

  * [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1)—Per card
  * [Embossing summary received](https://developers.pismo.io/events/docs/cards-embossing-summary-1)—End of process embossing summary

  ### Step 5—Retrieve generated file details

  Call the [List embossing files info ](https://developers.pismo.io/pismo-docs/reference/get-embossing-file-info)endpoint to retrieve generated file details for tracking purposes.

  ### Step 6—Download file

  Call the  [Get embossing file ](https://developers.pismo.io/pismo-docs/reference/get-embossing-download-file)endpoint (pismo.io) to download the file.
</details>

<details>
  <summary style={{ fontSize: "20px" }}><b>Noname cards</b></summary>

  Noname cards are batch-generated and not initially associated with customers, which occurs later.

  ### Step 1—Create noname card

  Call the [Create noname card bulk](https://developers.pismo.io/test-pismo-docs/reference/create-bulk-1) endpoint to create the noname card. Up to 1000 cards can be created with this endpoint.

  ### Step 2—Start noname bulk process

  Call the [Start noname card bulk process ](https://developers.pismo.io/pismo-docs/reference/start-bulk)endpoint to start the embossing process for noname cards.

  As card creation is asynchronous, the following event is generated:

  * [Card created ](https://developers.pismo.io/events/docs/cards-create-1)

  ### Step 3—Retrieve embossing configurations

  Retrieve the embossing configurations using the [Get org embosser info](https://developers.pismo.io/pismo-docs/reference/get-embossing-configurations-info) endpoint.

  ### Step 4—Start embossing process

  Call the [Start card embossing](https://developers.pismo.io/pismo-docs/reference/start-embossing) endpoint to begin the embossing process

  The following events are generated:

  * [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1)—Per card
  * [Embossing summary received](https://developers.pismo.io/events/docs/cards-embossing-summary-1)—End of process embossing summary

  ### Step 5—Retrieve generated file details

  Call the [List embossing files info ](https://developers.pismo.io/pismo-docs/reference/get-embossing-file-info)endpoint to retrieve generated file details for tracking purposes.

  ### Step 6—Download file

  Call the  [Get embossing file ](https://developers.pismo.io/pismo-docs/reference/get-embossing-download-file)endpoint (pismo.io) to download the file.
</details>

# Working with more than one embosser

You can work with more than one embosser. Below is the typical flow for making that happen.:

1. Pismo configures all embossing groups (with their respective schedules, embosser assignments, and program bindings) via a [Service request](https://developers.pismo.io/pismo-docs/docs/service-desk)  and meeting with your Pismo representative.
2. The `embossing_group` field names an embosser and indicates there is a mutual agreement between you, Pismo, and the embosser. All parties can propose the values, and all  agree on what to use.
3. You pass the appropriate `embossing_group` value in the [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) request to route the card to the correct embosser. If this field is not passed, the embosser specified as the default is used.

# Embossing rules

A nominal card may **NOT** be embossed  for the following reasons:

* Card's account does not have a registered address
* Address with special characters (non-UTF-8 standard characters)
* Printed name—No letters with accents, numbers, or special characters - only letters (a-z|A-Z) and space, as specified in the <a href="https://emvlab.org/emvtags/show/t5F20/" target="_blank">ISO EMV tag 5F20</a> for cardholder name.
* Does not have a `CREATED` status. Does not apply to on-demand customers, see below.
* The card password has not been updated, unless configured otherwise (refer to section following).

### Passwords

For each and every Pismo card, a random password is generated when the card is created.

#### Noname cards

You do not need to update the card password — the card can be sent for embossing with the random password generated at card creation time. If the issuer prompts the cardholder to change the password, it can be done, for example, when activating the card.

#### Nominal cards

* The issuer can assign a random password or work with the cardholder to update the password before being sent for embossing. This is  **required** for the card to be embossed.
* If the issuer works with on-demand, there is no need to change the password for the card to be embossed (refer to section below).

### On demand embossing - override card password updated requirement

By default, cards enter the embossing window when the card's password is updated. Once that happens, they are embossed in the next embossing window as specified in your embossing configuration.

If your embossing configuration includes the `ONDEMAND` option , the password update is no longer the trigger for the card to enter the next embossing window. On-demand customers can emboss cards with `NORMAL`, `BLOCKED`, `PENDING`, and `WARNING` statuses, in addition to `CREATED`.

With this option, there are three endpoints you can use to emboss the card:

* [Add card to next scheduled embossing](https://developers.pismo.io/pismo-docs/reference/put-cards-embossing)
* [Get encrypted card data for embossing](https://developers.pismo.io/pismo-docs/reference/post-generate-embossing)
* [Resend cards for embossing](https://developers.pismo.io/pismo-docs/reference/start-reembossing)

Talk to your Pismo representative about setting this or open a [JIRA ticket ](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket) with `type` = `Settings`.

**IMPORTANT:** Only call these endpoints **AFTER** the [Card can be added to next scheduled embossing](https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1) event is received. This event is generated when a card is created and all necessary asynchronous PCI configuration is done.

### Issuer Public Key (IPK) certificate

An <a href="https://en.wikipedia.org/wiki/Public_key_certificate" target="_blank">IPK certificate</a> is a digital certificate used in financial transactions, especially with Visa contactless cards, containing an issuer's public key. It is Certificate Authority (CA)-signed to enable secure validation for offline payments. It proves the card's authenticity and links it to a trusted issuer, allowing terminals to verify the card's data securely. In short, it's a digital ID for the bank that issues your card, ensuring trust in the payment system.

Pismo **does not** provide the IPK—the issuer or network, likely the issuer—is responsible for it. Providing this certificate for the embosser falls outside Pismo's scope.

### Pretty Good Privacy (PGP) key encryption

All card embossing files are encrypted using PGP keys where the embossing partner creates and holds the key pair, and Pismo uses the key's public component. The public key is sent to Pismo via a configuration Service Request. The card embossing process can only be started once the PGP key pair is created and configuration is complete. The embossing partner can decrypt the file using the private key they hold.

For more information on PGP encryption, refer to the [Pismo platform security guide](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide).

# Troubleshooting embossing errors

A card issuer might see the following errors. For all these errors except `card_status_invalid`, the card is automatically embossed after correction.

* `account_address_not_found`—You need to register the cardholder address.
* `account_address_inactive` —You need to activate the cardholder address.
* `account_phone_not_found`—If the client has a phone number sent in the embossing file, you need to register the phone number for the cardholder.
* `card_pci_password_unchanged`— f the customer updates the card password for embossing, you must also update the password.
* `card_status_invalid`—Card has invalid status for embossing. For ondemand, `CREATED`, `NORMAL`, `BLOCKED`, `WARNING` and `PENDING` statuses are allowed. Otherwise, only `CREATED`is allowed. For update password, only `CREATED` status is allowed. If necessary, you must create another card for the cardholder.
* `invalid_printed_name` —You must correct the printed name.
* `account_address_zipcode_invalid`—You must correct the cardholder's zip code/postal code.

For the following errors, you need to contact Pismo with a  [Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk) request:

* `account_not_found`
* `customer_not_found`
* `card_pci_not_found`
* `card_not_found`
* `card_type_invalid`
* `internal_error`
* `embossing_line_not_formatted`
* `embossing_line_not_encrypted`
* `embossing_line_invalid_format`
* `embossing_undelivered`
* `card_validation_error`

# Embossing API endpoints

You can use the following API endpoints to generate embossed cards:

* [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card)
* [Reissue physical card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue)
* [Create noname card bulk](https://developers.pismo.io/pismo-docs/reference/create-bulk)—After this call, you need to call [Start noname card bulk process](https://developers.pismo.io/pismo-docs/reference/start-bulk) to begin the embossing process.

All of these calls have an `embossing_custom_field`  you can use to send data to your embosser. This field is a string that can store up to **1000** characters, allowing you to personalize it with, for example, a delivery tracking code or  to indicate whether the card should be plastic or metal.

# Embossing events

Embossed cards generate the following sequence of events:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Event
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Card created](https://developers.pismo.io/events/docs/cards-create-1)
      </td>

      <td>
        The card has been created.
      </td>
    </tr>

    <tr>
      <td>
        [Card can be added to next scheduled embossing](https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1)
      </td>

      <td>
        This event indicates that a physical card is ready to be added to the next scheduled embossing according to the issuer's embossing settings. For nominal cards, you must either <a href="https://developers.pismo.io/pismo-docs/reference/put-v2-card-password">change the password</a> or <a href="https://developers.pismo.io/pismo-docs/reference/put-v1-update-pin-from-pinblock">change the password from PINblock</a> or <a href="https://developers.pismo.io/pismo-docs/reference/put-cards-embossing">add the card to the next scheduled embossing</a>.
      </td>
    </tr>

    <tr>
      <td>
        [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1)
      </td>

      <td>
        This event is generated for each card in the queue as it is being added to the file to be sent to the embosser or rejected. If rejected, the event data contains an error type and an error message.

        This event is emitted only in the embossing window timeframe when the embossing file is actually being generated. For example, for noname cards, the embossing window is at 1 am GMT-3, so the embossing-1 events are sent at approximately at this time. For named cards, they are generated in the timeframe of all the embossing windows set up to occur during the day for the specific client.
      </td>
    </tr>

    <tr>
      <td>
        [Embossing rejection file processed](https://developers.pismo.io/events/docs/cards-card-rejection-1)
      </td>

      <td>
        This  event is generated from the rejection return file that the embosser sends back to Pismo. Currently, the only embosser doing this is EM1.
      </td>
    </tr>

    <tr>
      <td>
        [Embossing summary received](https://developers.pismo.io/events/docs/cards-embossing-summary-1)
      </td>

      <td>
        Occurs when the embossing process is complete, providing summary information.
      </td>
    </tr>

    <tr>
      <td>
        [Card postage processed](https://developers.pismo.io/events/docs/cards-control-post-ingress-1)
      </td>

      <td>
        This event is generated when Pismo processes the postage control return file from the EM1 embosser.
      </td>
    </tr>
  </tbody>
</Table>

As described above, when a card is added to the file to be sent to an embosser or rejected, it generates an [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1) event. For a noname card bulk, this means that up to 10,000 events could potentially be generated.

**For example (success)**

See [Event data](https://developers.pismo.io/pismo-docs/docs/event-data) for more information about events.

See our [Data and reporting](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview) guide for more information on events and setting up event notifications.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /embossing/v1/cards/{cardId}` | `get-embossing-info` | Get nominal card embossing info | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-data |
| `PATCH /embossing/v1/cards/{cardId}` | `patch-embossing-group` | Update nominal card embossing group | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing |
| `GET /embossing/v1/cards/noname/{cardId}` | `get-noname-embossing-info` | Get noname card embossing info | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-data |
| `PATCH /embossing/v1/cards/noname/{cardId}` | `patch-noname-embossing-group` | Update noname card embossing group | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `PATCH /wallet/v2/cards/{cardId}` | `patch-v2-card` | Update card information | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PUT /embossing/v1/cards/{cardId}/embossing` | `put-cards-embossing` | Add card to next scheduled embossing | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing |
| `DELETE /embossing/v1/cards/{cardId}/embossing` | `delete-cards-embossing` | Delete card from next scheduled embossing | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing |
| `GET /embossing/v1/configurations/info` | `get-embossing-configurations-info` | Get org embosser info | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-data |
| `POST /embossing/v1/triggers/embossing` | `start-embossing` | Start card embossing | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing |
| `GET /embossing/v1/file-info` | `get-embossing-file-info` | List embossing files info | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-data |
| `GET /embossing/v1/download-file` | `get-embossing-download-file` | Get embossing file | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-data |
| `POST /cards/v1/bulks/{bulkID}/start` | `start-bulk` | Start noname card bulk process | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `POST /embossing/v1/cards/generate-embossing` | `post-generate-embossing` | Get nominal encrypted card data for embossing | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-encrypted |
| `POST /embossing/v1/cards/reembossing` | `start-reembossing` | Resend cards for embossing | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /cards/v1/bulks` | `create-bulk` | Create noname card bulk | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |

### Operation essentials

- **`GET /embossing/v1/cards/{cardId}`** (`get-embossing-info`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 400, 404; error codes in examples none; events none listed.
- **`PATCH /embossing/v1/cards/{cardId}`** (`patch-embossing-group`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 204, 400, 404, 409; error codes in examples none; events none listed.
- **`GET /embossing/v1/cards/noname/{cardId}`** (`get-noname-embossing-info`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 400, 404; error codes in examples none; events none listed.
- **`PATCH /embossing/v1/cards/noname/{cardId}`** (`patch-noname-embossing-group`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 204, 400, 404, 409; error codes in examples none; events none listed.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`PATCH /wallet/v2/cards/{cardId}`** (`patch-v2-card`): security `BearerAuth`; required parameters `cardId` (path), `x-customer-id` (header); required body fields none declared; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-update-1`.
- **`POST /wallet/v2/cards`** (`post-v2-card`): security `BearerAuth`; required parameters `x-customer-id` (header); required body fields `name`, `type`; response statuses 200, 201, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`.
- **`PUT /embossing/v1/cards/{cardId}/embossing`** (`put-cards-embossing`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 202, 400, 401, 404, 406, 500; error codes in examples none; events `cards-embossing-card-ingress-1`.
- **`DELETE /embossing/v1/cards/{cardId}/embossing`** (`delete-cards-embossing`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 202, 400, 401, 404, 406, 500; error codes in examples none; events none listed.
- **`GET /embossing/v1/configurations/info`** (`get-embossing-configurations-info`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 404; error codes in examples none; events none listed.
- **`POST /embossing/v1/triggers/embossing`** (`start-embossing`): security `BearerAuth`; required parameters none declared; required body fields `config_id`; response statuses 202, 400; error codes in examples none; events none listed.
- **`GET /embossing/v1/file-info`** (`get-embossing-file-info`): security `BearerAuth`; required parameters `beginDate` (query), `endDate` (query); required body fields none declared; response statuses 200, 204, 400; error codes in examples none; events none listed.
- **`GET /embossing/v1/download-file`** (`get-embossing-download-file`): security `BearerAuth`; required parameters `fileName` (query); required body fields none declared; response statuses 200, 400; error codes in examples none; events `cards-embossing-1`, `cards-embossing-summary-1`.
- **`POST /cards/v1/bulks/{bulkID}/start`** (`start-bulk`): security `BearerAuth`; required parameters `bulkID` (path); required body fields none declared; response statuses 202, 400, 404, 409, 500; error codes in examples none; events `cards-create-1`.
- **`POST /embossing/v1/cards/generate-embossing`** (`post-generate-embossing`): security `BearerAuth`; required parameters none declared; required body fields `card_id`, `iv`, `key_id`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `cards-embossing-1`.
- **`POST /embossing/v1/cards/reembossing`** (`start-reembossing`): security `BearerAuth`; required parameters none declared; required body fields `cards`; response statuses 202, 400, 401, 500; error codes in examples none; events `cards-reembossing-1`.
- **`POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue`** (`post-v1-card-reissue`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path); required body fields `reason_id`; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`, `cards-update-1`.
- **`POST /cards/v1/bulks`** (`create-bulk`): security `BearerAuth`; required parameters none declared; required body fields `external_ids`, `program_id`; response statuses 201, 400, 409, 500; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-card-reissue` | `cards-create-1` |
| `post-v2-card` | `cards-create-1` |
| `start-bulk` | `cards-create-1` |
| `get-embossing-download-file` | `cards-embossing-1` |
| `post-generate-embossing` | `cards-embossing-1` |
| `put-cards-embossing` | `cards-embossing-card-ingress-1` |
| `get-embossing-download-file` | `cards-embossing-summary-1` |
| `start-reembossing` | `cards-reembossing-1` |
| `patch-v2-card` | `cards-update-1` |
| `post-v1-card-reissue` | `cards-update-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `cards-create-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-create-1 | 4 | KU-EVT-catalogue-cards |
| `cards-embossing-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-1 | 5 | KU-EVT-catalogue-cards |
| `cards-embossing-card-ingress-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1 | 2 | KU-EVT-catalogue-cards |
| `cards-embossing-summary-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-embossing-summary-1 | 1 | KU-EVT-catalogue-cards |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/physical-card-embossing.md`: updatedAt 2026-07-21T18:09:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 6 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/physical-card-embossing.md` | whole document | https://developers.pismo.io/pismo-docs/docs/physical-card-embossing | `7521b7feeb28d303…` | 2026-07-21T18:09:22.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--embossing` — API reference: Card issuing - Cards — Embossing
- `KU-API-card-issuing-cards--embossing-data` — API reference: Card issuing - Cards — Embossing data
- `KU-API-card-issuing-cards--embossing-encrypted` — API reference: Card issuing - Cards — Embossing encrypted
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-AUTH-pismo-platform-security-guide` — Security guide for Pismo platform
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-data-events-concepts` — Data events: concepts and event-generating APIs
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
