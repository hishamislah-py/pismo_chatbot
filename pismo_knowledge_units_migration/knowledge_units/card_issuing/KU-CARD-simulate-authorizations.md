---
ku_id: KU-CARD-simulate-authorizations
title: Simulate authorizations
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/simulate-authorizations.md
  sha256: 2970bf47745bdbca9a572befd9325be28f85317e191c000dc3d7cdc4e66ceb48
  url: https://developers.pismo.io/pismo-docs/docs/simulate-authorizations
  role: primary_guide
  updated_at: '2026-03-18T15:20:57.000Z'
operations:
- cancel-network-authorizations
- post_v1-authorizations
related_kus:
- KU-API-card-issuing-authorization--authorizations
- KU-CARD-anti-fraud-integration
- KU-CARD-authorization-events
- KU-CARD-clearing
- KU-CARD-full-and-zero-balance-workflows
- KU-CORE-processing-codes-and-transaction-types
- KU-ERR-validation-code-definitions
- KU-ERR-validation-codes-for-authorization-events-part-01
- KU-ERR-validation-codes-for-authorization-events-part-02
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Simulate authorizations

**KU ID:** `KU-CARD-simulate-authorizations` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/simulate-authorizations.md`:

> Walk-through of different scenarios to simulate authorizations.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/simulate-authorizations.md`: Simulate authorizations; Simulation features; Run the initial authorization request (authorization/base I); Cancel the transaction via an authorization request; Confirm the authorization (clearing/base II); Cancel the transaction via clearing; Other examples; Related pages

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/simulate-authorizations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/simulate-authorizations · updatedAt: 2026-03-18T15:20:57.000Z

<!-- source:begin path=docs/card-issuing/simulate-authorizations.md part=0-end -->

# Simulate authorizations

Walk-through of different scenarios to simulate authorizations.

At times, you may want to simulate card transactions in the sandbox (test) environment when implementing a new product, testing a new condition, or integration.

You can simulate a real-world authorization from the network in the sandbox environment with the [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint. This simulation does not go through all the card network services as it would in production, but it does check for card status and balance. The call gives you a chance to see how Pismo might respond to a network authorization. The fields returned can be used to cancel or confirm the request with the same endpoint.

The simulator can be used to generate a [network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event that you can receive and view , which can occur, in production, when Pismo cancels or confirms an authorization. The simulator also gives you a chance to test out connectivity to your [anti-fraud webhook URL](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration).

You can also use Simulate authorization endpoint to cancel (total or partial) the simulated authorization in the test environment. To cancel in the production environments, use the [Cancel authorization](https://developers.pismo.io/pismo-docs/reference/cancel-network-authorizations) endpoint.

> 📘
>
> The `Simulate authorization` endpoint does not issue a [clearing event](https://developers.pismo.io/pismo-docs/docs/clearingbase). When you use the endpoint for simulation with `MTI Clearing (1240)`, it generates a [network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event with the category **CONFIRMATION**, which represents the clearing.

In production, a Pismo-issued card transaction executes a number of interlinked services from the PIN pad to the acquirer, to Pismo, to the issuer, and back again to the originating PIN pad.

## Simulation features

You can use the [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint to run four scenarios:

**Base 1 (online)**

1. Run the initial authorization request (authorization/base 1)
2. Cancel the transaction via an authorization request

**Base II (confirmation)**

3. Confirm the authorization (clearing/base II)
4. Cancel the transaction via clearing

Note that in order for an authorization to show as a transaction (for example, in the client statement or via the [List transactions](https://developers.pismo.io/pismo-docs/docs/listtransactions) endpoint, it has to first be approved in Base I then confirmed in Base II. Be sure to run both simulations if this is what you want to test.

> 📘 Simulation events
>
> The simulator allows you to verify your event notification setup. For more information on setting this up, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).
>
> For authorization confirmation and cancellation, the simulator generates a [network authorization](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event in the EXT environment. For more information on this event,  [click here](https://developers.pismo.io/pismo-docs/docs/authorization-events#network-authorization-event).
>
> In production, this event is generated during step 6 in the [Full and zero balance workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).
>
> The simulator does **NOT** generate the following:
>
> * Network authorization [iso8583-message-1](https://developers.pismo.io/events/docs/networktransactions-iso8583-message-1) event
> * Clearing/base II (raw messages) events
>   * [raw\_credit\_mastercard-1](https://developers.pismo.io/events/docs/authorization-raw-credit-mastercard-1)
>   * [raw\_debit\_mastercard-1](https://developers.pismo.io/events/docs/authorization-raw-debit-mastercard-1)
>   * [raw\_credit\_visa-1](https://developers.pismo.io/events/docs/authorization-raw-credit-visa-1)
>   * [raw\_debit\_visa-1](https://developers.pismo.io/events/docs/authorization-raw-debit-visa-1)
> * Card [network-authorization-1](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) return event
>
> For more information on these events, see [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events).

You can go through the authorization simulation in the following order:

1. Run the initial authorization request (authorization/base I). (See below)
2. Use the response's `authorization_code` to [cancel the transaction via an authorization request](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations#cancel-the-transaction-via-an-authorization-request).
3. Use the same `authorization_code` to reopen and [confirm the transaction (clearing/base II)](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations#confirm-the-authorization-clearingbase-ii).
4. [Cancel the transaction via clearing](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations#cancel-the-transaction-via-clearing).

# Run the initial authorization request (authorization/base I)

To begin authorization, start with an authorization/base I request similar to the following:

```json Sample request
curl -L -X  POST 'https://api-sandbox.pismolabs.io/networktransactions/v1/authorizations' 
-H 'Accept: application/json'
-H 'Content-Type: application/json' 
-H 'x-tenant: <Org ID>' 
-d '{
  "caller": "visa",
  "card_id": <card ID>,
  "local_amount": 501,
  "local_currency": "986",
  "settlement_amount": 501,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "00",
  "response_code": "00",
  "account_type": "30",
  "mti": "0100",
  "anti_fraud_url", <Your anti-fraud webhook>
  "merchant": {
    "name": "MERCHANT TEST",
    "city": "MERCHANT CITY",
    "country": "BR",
    "code": "5542"
  },
  "installments": {
    "is_crediario": true,
    "number": 5,
    "with_interest": false
  }
}
```

In this request, the following fields are important:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Values
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mti
      </td>

      <td>
        `0100`: auth. request\
        `0110`: 	auth. response 	\
        `0120`: auth. advice\
        ...
      </td>

      <td>
        Message type indicator. For more information, see <a href="https://en.wikipedia.org/wiki/ISO_8583#Message_type_indicator_(MTI)" target="_blank">MTI</a>
      </td>
    </tr>

    <tr>
      <td>
        anti\_fraud\_url
      </td>

      <td>
        URL
      </td>

      <td>
        Your anti-fraud webhook URL. For example: [https://api.ext.client.info/webhook/provider/client/authorize](https://api.ext.client.info/webhook/provider/client/authorize)
      </td>
    </tr>

    <tr>
      <td>
        processing\_code
      </td>

      <td>
        \- `00`: p urchase

        * `01`: withdrawal
        * `20`: credit (also used to simulate cancellation)
        * `28`: payment
      </td>

      <td>
        Type of operation to be performed. For more information, see [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types)
      </td>
    </tr>

    <tr>
      <td>
        local\_currency and settlement\_currency
      </td>

      <td>
        String\
        Examples:\
        `986` - Brazil\
        `840` - US
      </td>

      <td>
        ISO 4217 currency codes
      </td>
    </tr>

    <tr>
      <td>
        entry\_mode
      </td>

      <td>
        string\
        Example: `901`
      </td>

      <td>
        This field is required and must have 3 or 4 digits. For example, try `901` or `9010` for magnetic stripe transaction simulation.
      </td>
    </tr>

    <tr>
      <td>
        installments
      </td>

      <td>
        object(s)
      </td>

      <td>
        Object to send the installment information.

        * \*Note:\*\* For cash transactions, do not send the installments object.
      </td>
    </tr>

    <tr>
      <td>
            is\_crediario
      </td>

      <td>
        `true` or `false`
      </td>

      <td>
        Is this a crediário transaction - a Brazil specific installment plan?
      </td>
    </tr>

    <tr>
      <td>
            number
      </td>

      <td>
        Numeric value
      </td>

      <td>
        Number of installments.
      </td>
    </tr>

    <tr>
      <td>
            with\_interest
      </td>

      <td>
        `true` or `false`
      </td>

      <td>
        Is this a purchase with interest or without interest?
      </td>
    </tr>

    <tr>
      <td>
        merchant
      </td>

      <td>
        object
      </td>

      <td />
    </tr>

    <tr>
      <td>
            country
      </td>

      <td>
        Examples:\
        `BR` - Brazil\
        `US` - United States
      </td>

      <td>
        ISO 3166 country codes
      </td>
    </tr>
  </tbody>
</Table>

> 📘 FRH - POS (point-of-sale) entry mode validation
>
> FRH - POS is the denial list for terminal capability validation (POS or input device) and entry mode. This validation checks how the card data was acquired (card machine, online purchase, NFC, etc.) and the entry mode information. For example, in e-commerce, it’s not possible to retrieve the card chip data, so it’s not a valid entry mode and should be denied. For Visa, entry mode is in Field 22. For Mastercard, it's in DE 61.
>
> For full details on entry mode validation and possible codes, refer to the [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#frh---pos-point-of-sale-entry-mode-validation) guide.

You can change the corresponding parameters according to the different scenarios as shown in the following table:

| Scenario                 | Parameters                                                                                                                    | Additional notes                                                                                                                             |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Domestic purchase        | `"processing_code": "00", "local_currency": "986",`                                                                           | `986` for the Brazilian real.                                                                                                                |
| Domestic withdrawal      | `"processing_code": "01", "local_currency": "986",`                                                                           | `986` for the Brazilian real.                                                                                                                |
| International purchase   | `"processing_code": "00", "local_currency": "840",`                                                                           | `840` for the US dollar. If this value is anything other than `840`, add the `settlement_amount` and `settlement_currency` values as needed. |
| International withdrawal | `"processing_code": "01", "local_currency": "840",`                                                                           | `840` for the US dollar. Update the transaction's `local_currency` code as needed.                                                           |
| Installment purchase     | `"processing_code": "00", "installments": {                 "is_crediario": true, 		"number": 2, 		"with_interest": true 	},` |                                                                                                                                              |

> 🚧 Important considerations for Processing Codes
>
> It is highly recommended to never use custom processing codes. Instead, **always use** the standardized processing codes provided by the card network, such as `00`, `20`, `28`, `01`, among others. The platform itself will transform these into custom processing codes as needed.
>
> **Never use** processing codes such as `003100` or `003800`, among others.

After you send the initial sample authorization request, you will receive a response similar to the following:

```json Sample response (success)
{
  "mti": "0110",
  "authorization_code": "EK6JXC",
  "response_code": "57",
  "authorization_date_time": "2023-02-21T10:49:23",
  "retrieval_reference_number": "",
  "custom_code": "ANF",
  "authorization_id": 51123840,
  "account_id": <account ID>,
  "mode_type": "CREDIT",
  "card_mode": "CREDIT",
  "installment_value": 0,
  "interest_rate": 0,
  "number_of_installments": 5,
  "contract_amount": 0,
  "principal_amount": 0,
  "crediario_responses": [],
  "is_domestic_transaction": true, // Not returned for international transactions
  "settlement_amount": "501.00"
}
```

Save the response's `authorization_code`  to use in subsequent steps.

> 📘 Response codes
>
> Approved transactions generate the response code `00`. Any other response code indicates a rejected transaction. Some common response codes for rejected transactions are:
>
> * `14`: no card found or no acceptances configured
> * `51`: insufficient funds
> * `57`: card not active
> * `96`: system failure or issuer timeout
>
> In addition to the response code, it is important to note the custom code. The platform uses the same response code for some issuers, and, in those cases, the difference is specified by the custom code. For example, with Mastercard:
>
> * `response_code 14` and `custom_code FR7`: no card found
> * `response_code 51` and `custom_code 810`: insufficient funds
> * `response_code 57` and `custom_code UBT`: card not active
> * `response_code 96` and `custom_code OP1`: system failure
>
> For the full list of response codes and custom codes for rejected transactions, see [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events).

# Cancel the transaction via an authorization request

At this stage, you can cancel the transaction in the following way:

1. In the same request as above, add the `authorization_code` from the first response.
2. Change the `mti` value to `0400`(reversal request).
3. Run the request.

```json Cancel authorization request
{
  "caller": "visa",
  "card_id": <card ID>,
  "local_amount": 501,
  "local_currency": "986",
  "settlement_amount": 151,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "00",
  "response_code": "00",
  "account_type": "30",
  "mti": "0400",
  "authorization_code": "EK6JXC",
  "merchant": {
		"name": "MERCHANT TEST",
		"city": "MERCHANT CITY",
		"country": "BR",
		"code": "5542"
  },
  "installments": {
		"is_crediario": true,
		"number": 5,
		"with_interest": false
    }
}
```

# Confirm the authorization (clearing/base II)

The authorization confirmation, known as clearing/base II, is the process of finalizing the transaction.  To simulate the clearing process, you need to add certain purchase payload fields to the same transactions endpoint.

> 📘
>
> This simulation of the clearing process is not possible for the Zero Balance solutions since in this case the authorization confirmation is performed by the clearing/base II (raw messages) events from the card network.

To simulate the clearing process, configure the request as follows:

1. Set the `mti` field to `clearing`.
2. Keep the same `processing_code` as in the initial request.
3. Add the following fields:
   * `authorization_code` with the same value as in the first response
   * `processing_julian_date` with a valid date (ydddd)
   * `message_number`
   * `acquirer_reference_number`
4. Run the request.

The following fields are important for the confirmation step in clearing/base II:

| Field                       | Value        | Description                                                                                                                                                                                                   |
| :-------------------------- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mti                         | `clearing`   | Defines the message type. In case of a transaction confirmation, the text should be `clearing`.                                                                                                               |
| authorization\_code         | `EK6JXC`     | This field is returned on the initial authorization request and must be used on the confirmation request.                                                                                                     |
| acquirer\_reference\_number | `ABC123YZ25` | This is a value that Pismo receives from the acquirer.                                                                                                                                                        |
| message\_number             | `02`         | In the production environment, this is a unique sequential number assigned to the clearing message in the card network clearing file. In the simulation, you can use any numeric value.                       |
| processing\_julian\_date    | `1239`       | Date in flag format YDDD, where the last digit of the year is concatenated with the number corresponding to the day in the calendar. For example, February 26, 2021 is 1057, where 2021 is 1 and 26/02 is 57. |

The other payload fields must have the same values as the initial authorization request to keep the original values from Authorization/Base I. If any field values in the clearing request are different from the values in the initial request, these values get updated since the information from the clearing confirmation takes precedence.

Sample confirmation clearing request:

```json Sample confirmation clearing request
{
  "caller": "visa",
  "card_id": <card ID>,
  "local_amount": 501,
  "local_currency": "986",
  "settlement_amount": 151,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "00",
  "response_code": "00",
  "account_type": "30",
  "mti": "clearing",
  "authorization_code": "EK6JXC",
  "acquirer_reference_number": "ABC123YZ25",
  "message_number": "02",
  "processing_julian_date": "1239",
  "merchant": {
		"name": "MERCHANT TEST",
		"city": "MERCHANT CITY",
		"country": "BR",
		"code": "5542"
  },
  "installments": {
		"is_crediario": true,
		"number": 5,
		"with_interest": false
    }
}
```

> 🚧 Other important considerations for the clearing process:
>
> * If you need to process more than one clearing for the same authorization, make sure that at least one of the following fields - `message_number`, `processing_julian_date`, or `acquirer_reference_number` - is different from the previous message.
> * Clearing messages for the same purchase should be processed at least 2 minutes apart. Processing is denied if the second message is sent at a shorter interval.

# Cancel the transaction via clearing

Another way to cancel a transaction is via clearing:

1. Change the `processing_code` field value to `20`.
2. Keep the `mti` value as `clearing`.
3. Keep the same `authorization_code`.
4. Change one of the values in the `message_number`, `processing_julian_date`, or `acquirer_reference_number` fields, which indicates that it is a new clearing message.

To generate a partial cancellation, send the clearing message with the field `local_amount` with a value lower than the authorization/confirmation value.

```json Partial cancellation request
{
  "caller": "visa",
  "card_id": <card ID>,
  "local_amount": 250,
  "local_currency": "986",
  "settlement_amount": 151,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "20",
  "response_code": "00",
  "account_type": "30",
  "mti": "clearing",
  "authorization_code": "EK6JXC",
  "acquirer_reference_number": "ABC123YZ25",
  "message_number": "03",
  "processing_julian_date": "1239",
  "merchant": {
		"name": "MERCHANT TEST",
		"city": "MERCHANT CITY",
		"country": "BR",
		"code": "5542"
  },
  "installments": {
		"is_crediario": true,
		"number": 5,
		"with_interest": false
    }
}
```

# Other examples

The [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint has other example payloads you can view:

<Image alt="Screen capture of the Simulate authorization endpoint payloads." align="center" className="border" border={true} src="https://files.readme.io/1bafd5b-examplesSim.PNG" />

# Related pages

[API reference / Simulate authorizations](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /networktransactions/v1/authorizations` | `post_v1-authorizations` | Simulate authorization | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /direct-network-transactions/v1/cancellation` | `cancel-network-authorizations` | Cancel authorization | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |

### Operation essentials

- **`POST /networktransactions/v1/authorizations`** (`post_v1-authorizations`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `networktransactions-network-authorization-1`.
- **`POST /direct-network-transactions/v1/cancellation`** (`cancel-network-authorizations`): security `BearerAuth`; required parameters none declared; required body fields `network_authorization_id`, `authorization_code`, `card_id`; response statuses 200, 400, 403, 404, 409, 500; error codes in examples none; events `networktransactions-network-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `cancel-network-authorizations` | `networktransactions-network-authorization-1` |
| `post_v1-authorizations` | `networktransactions-network-authorization-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/simulate-authorizations.md`: updatedAt 2026-03-18T15:20:57.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 6 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/simulate-authorizations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/simulate-authorizations | `2970bf47745bdbca…` | 2026-03-18T15:20:57.000Z |

## Related knowledge units

- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-CARD-anti-fraud-integration` — Anti-fraud integration
- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-ERR-validation-code-definitions` — Validation code definitions
- `KU-ERR-validation-codes-for-authorization-events-part-01` — Validation codes for authorization events (part 1 of 2)
- `KU-ERR-validation-codes-for-authorization-events-part-02` — Validation codes for authorization events (part 2 of 2)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
