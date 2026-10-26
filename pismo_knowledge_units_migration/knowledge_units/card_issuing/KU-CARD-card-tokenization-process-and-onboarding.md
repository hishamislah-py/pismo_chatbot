---
ku_id: KU-CARD-card-tokenization-process-and-onboarding
title: Card tokenization process and onboarding
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/card-tokenization-process-and-onboarding.md
  sha256: 8967390a01eea7e3fa7999e6509231838d5c75fbee4de3d3e6fb97ef664e9362
  url: https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding
  role: primary_guide
  updated_at: '2026-04-22T15:19:46.000Z'
operations:
- get-card-token-info
- gettokeninfo
- performtokenop
- post-encrypted-applepay-data
- post-v1-card-reissue
- post-v1-cards-card-id-network-tokens-profile
- post-wallet-data
- post-wallet-data-samsung
- transfertokens
related_kus:
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-tokenization--card-lifecycle
- KU-API-card-issuing-tokenization--network-card-profile
- KU-API-card-issuing-tokenization--pre-digitalization
- KU-API-card-issuing-tokenization--token-lifecycle
- KU-CARD-card-lifecycle-and-statuses
- KU-CARD-card-network-integration
- KU-CARD-card-tokenization-flow-and-events
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-other-domains
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Card tokenization process and onboarding

**KU ID:** `KU-CARD-card-tokenization-process-and-onboarding` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/card-tokenization-process-and-onboarding.md`:

> The card tokenization process with Pismo involves the following participants:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/card-tokenization-process-and-onboarding.md`: Card tokenization process and onboarding; Issuer involvement in tokenization process; Step 1 - Business planning; Step 2 - Register with your wallet provider and card network; Step 3 - Implement the Pismo events stream; Step 4 - Configure Pismo tokenization; Step 5 - Test and launch; Token provisioning; Manual provisioning authentication; Application to application (App2App); SMS OTP; Email OTP; Call center; Push provisioning detailed flow; Tokenizing Pismo card using wallet SDK; Token lifecyle; Identifying a tokenized transaction; Primary account number (PAN) update

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/card-tokenization-process-and-onboarding.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding · updatedAt: 2026-04-22T15:19:46.000Z

<!-- source:begin path=docs/card-issuing/card-tokenization-process-and-onboarding.md part=0-end -->

# Card tokenization process and onboarding

The card tokenization process with Pismo involves the following participants:

* **Card network**—The entity (Visa, Mastercard, and so on) responsible for generating the token using card sensitive information such as the Primary Account Number (PAN). The network manages the tokenization and authorization process and is involved throughout.
* **Issuer token service providers**—I-TSPs are responsible for token management. A TSP provides the APIs and resources necessary for provisioning and lifecycle flow according to each network's rules and certification.  Pismo is an I-TSP.
* **Token requestor**—All entities that request payment tokens in return for a payment card. These entities include wallets, issuer apps, and e-commerce sites such as Netflix.
* **Issuers**—Also known as Payment Service Providers (PSP). Makes decisions on each tokenization request based on several parameters to ensure that tokenized cards are issued to the rightful owners. As with physical cards, the Issuer must also handle the life cycle management of existing tokens. To be able to issue these cards and participate in these processes, the issuer must connect to a I-TSP such as Pismo.

As an I-TSP, Pismo provides network-agnostic API endpoints that can handle tokenization requests and responses for different networks. However, we also account for network-specific differences. Our solution provides different payloads for each network in the events stream, including network-specific metadata that provides additional context about the token and its status, such as the network identifier, tokenization scheme, and token expiration date. This approach helps simplify the development process for issuers and processors and improves the user experience for customers using digital wallets for payments.

# Issuer involvement in tokenization process

As an issuer, you can do three things as part of the tokenization process.

> 📘 Post-setup
>
> Note that this is after setup with Pismo and the card networks is completed and the tokenization process is in place. Refer to **Getting started with tokenization** below  for more information on getting this process set up.

1. [Assign the network card profile](https://developers.pismo.io/pismo-docs/reference/post-v1-cards-card-id-network-tokens-profile)—The network card profile determines such things as how the card is visually displayed in a mobile payment app. As the issuer, you need to configure network profiles with the card network.
2. [Code your own tokenization anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#client-anti-fraud-webhook-for-card-tokenization)—Pismo calls this webhook during the tokenization process. This webhook allows you to perform your own validations, in addition to Pismo's, and set the authentication method, if any.
3. Monitor the events generated in the tokenization process—Once you have set up [data and reporting](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview), you can monitor the events that Pismo and the network generate during tokenization. Refer to [Card tokenization flow and events](https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events) for more information. **The sequence diagrams in this guide show where events are emitted in tokenization flows.**

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Getting started with tokenization</summary>

  Follow these general steps to tokenize your cards for third-party wallets such as Google or Apple Pay.

  ## Step 1 - Business planning

  Research the marketplace and speak to your Pismo and network representatives about what you would like to do including what wallets you want to offer to your cardholders.

  Define your implementation process and consider the following:

  * Authentication methods you want to implement.
  * Whether you want to code your own [anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#client-anti-fraud-webhook-for-card-tokenization)
  * Familiarize yourself with Pismo's tokenization endpoints and determine how and when you are going to call them

  ## Step 2 - Register with your wallet provider and card network

  Register with your wallet provider as a participating issuer. During the registration process, you will need to provide information about your company, your card products, and your technical capabilities.

  After registration, you need to obtain certifications from the card networks and your wallet provider to validate your integration and compliance with their respective standards. This can be part of [Card network certification](https://developers.pismo.io/pismo-docs/docs/network-certification).

  ## Step 3 - Implement the Pismo events stream

  During tokenization, you'll need to monitor the events stream for [tokenization flows](https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events). This involves setting up your [data reporting and monitoring](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview) to receive  notifications about tokenization events such as token creation, suspension, and deletion.

  ## Step 4 - Configure Pismo tokenization

  Pismo tokenization parameters are configured on a program basis. For most implementations it is necessary to exchange keys or certificates with the network. Talk to your Pismo representative and get the necessary information to precede with configuration and security.

  ## Step 5 - Test and launch

  After completing the integration, perform testing to ensure that your tokenized cards work correctly with your digital wallet provider.
</details>

# Token provisioning

There are two ways to provision a token :

* **Manual provisioning**—Cardholder enters card data directly into a wallet app to initiate provisioning.
* **Push provisioning**—Cardholder initiates provisioning using an issuer app.

<details>
  <summary><b>Manual provisioning flow</b></summary>

  <Image align="center" src="https://files.readme.io/bbcabe25c4da18dc932170006ec260f1c9b77a38d7be164b25bb9787c2d156c0-Manual_Provisioning.png" alt="Token provisioning - Manual and Push" />
</details>

<details>
  <summary><b>Push provisioning flow</b></summary>

  <Image align="center" src="https://files.readme.io/8bfd947ce00a615a368a7973a3afce4bb2727592a0d6cb17f1c47d63ab491934-Push_Provisioning.png" alt="Push provisioning" />
</details>

## Manual provisioning authentication

There are 4 ways, during the tokenization process with Pismo, that a cardholder can be asked or challenged to verify their identity.

* **Application to application (App2App)**—Pismo redirects cardholder to the issuer's app for authentication.
* **SMS one-time password (OTP)**—Pismo sends authentication request via  text message.
* **E-mail OTP**—Pismo sends authentication request via email.
* **Call center**—Pismo redirects cardholder to call center for authorization.

### Application to application (App2App)

**Key points:**

* To offer this method, the  issuer app’s URL has to be registered with Pismo
* Pismo is not involved on the wallet's request to the issuers app, or the app's cardholder authentication.
* To activate the token, use the [Perform token operation ](https://developers.pismo.io/pismo-docs/reference/performtokenop)endpoint, `operation_type` = `CARDHOLDER_SETUP_APP_TO_APP`for Mastercard and `CALL_CENTER_ACTIVATION` for Visa.
* If other manual authentication method is registered, all the options are displayed for the cardholder to select.

<details>
  <summary><b>Visa</b></summary>

  <Image align="center" src="https://files.readme.io/75a1441e6f50d8d855950dcc6323b05c34d109a04fd056fd8878545b0fd4bc3b-Visa_App_to_App.png" alt="Visa App2App provisioning" />
</details>

<details>
  <summary><b>Mastercard</b></summary>

  <Image align="center" src="https://files.readme.io/823b4c4c966594ca3a722057a1730ee80012d7e7b8acd413947df9e729942846-Mastercard_App2App.png" alt="Mastercard App2App provisioning" />
</details>

### SMS OTP

**Key points**

* To offer this method, the cardholder's phone number has to be registered with Pismo
* If you want to send the SMS to your cardholder, the one-time password (OTP) value is delivered to you in an [event](https://developers.pismo.io/events/docs/cards-tokenization-notification-1)
* The issuer defines the SMS template (140 chars max)
* If other manual authentication method is registered, all options are displayed for the cardholder to select

**Note**: Pismo’s SMS sending service is not available in all regions, please consult your representative to confirm

<details>
  <summary><b>Visa</b></summary>

  <Image align="center" src="https://files.readme.io/dee3e20f23bcc1b24fe2cc77f9ee5baee0846a6cf863a2f20cb6187d671e469a-Visa_SMS_OTP.png" alt="Visa SMS OTP flow" />
</details>

<details>
  <summary><b>Mastercard</b></summary>

  <Image align="center" src="https://files.readme.io/e3457efc072315cb3fec971fc8b705ee1a9178a3b1378269d066918baf412445-Mastercard_SMS_OTP.png" alt="Mastercard SMS OTP flow" />
</details>

### Email OTP

**Key points:**

* To offer this method, the cardholder's  email has to be registered with Pismo
* The issuer is responsible for delivering the one-time password (OTP) code in an email
* If other manual authentication method is registered, all the options are displayed for the cardholder to select

<details>
  <summary><b>Visa</b></summary>

  <Image align="center" src="https://files.readme.io/f048c0fcadfce5641e6e2461f0b19c7dcab2e79362ba051006fd5707521c74ac-Visa_OTP_Mail.png" alt="Visa Email OTP flow" />
</details>

<details>
  <summary><b>Mastercard</b></summary>

  <Image align="center" src="https://files.readme.io/81f8a14338295ad7e44aafd465ea6b94e740fdc130d9166dde5e15bdbdc249c1-Mastercard_OTP_Mail.png" alt="Mastercard Email OTP flow" />
</details>

### Call center

**Key points**

* The issuer is responsible for the call center service
* After call center verification, activate the token using the [Perform token operation](https://developers.pismo.io/pismo-docs/reference/performtokenop) endpoint, `operation_type` = `CALL_CENTER_ACTIVATION`
* If other manual authentication method is registered, all the options will be displayed for the cardholder to select

<details>
  <summary><b>Visa</b></summary>

  <Image align="center" src="https://files.readme.io/e2ec7a72d97d390b5c8fff446a884b71b1c89f46ed36e5770215a6cb1bb329dc-Visa_Call_Center.png" alt="Visa Call Center flow" />
</details>

<details>
  <summary><b>Mastercard</b></summary>

  <Image align="center" src="https://files.readme.io/8e0766b9fb3d17ac7bcdf56a08aa50808561496116e1ae4f13391cb9a65c85d2-Mastercard_Call_Center.png" alt="Mastercard Call Center flow" />
</details>

## Push provisioning detailed flow

Also known as ***in-app provisioning***. In this scenario, the cardholder initiates provisioning using an issuer app.  The issuer has to install the wallet's SDK on their app for this integration, and use Pismo’s endpoints to generate an authentication value that contains the card information encrypted with keys/certificates that are known to the wallet and network. The issuer passes this value to the wallet SDK.

<details>
  <summary><b>Visa Google Pay push provisioning</b></summary>

  <Image align="center" src="https://files.readme.io/9bf2189c74b7f27b7612f0b98d14dbf13e1acc80e2f7a9c8f55c00d519522d65-Google_Visa_Push_Provisioning.png" alt="Visa Google Pay push provisioning" />
</details>

<details>
  <summary><b>Mastercard Google Pay push provisioning</b></summary>

  <Image align="center" src="https://files.readme.io/e2aea0e235b0c6c7d7fca5e4b82b0d5f72d81cd66002b2173a31b5c6310c5157-Google_Mastercard_Push_Provisioning.png" alt="Mastercard Google Pay push provisioning" />
</details>

<details>
  <summary><b>Visa Apple Pay push provisioning</b></summary>

  <Image align="center" src="https://files.readme.io/e9a3eabb3b9cb1442215c033e47a95225d0ac71ce7b97a42a64b022b18583bdb-Apple_Visa_Push_Provisioning.png" alt="Visa Apple Pay push provisioning" />
</details>

<details>
  <summary><b>Mastercard Apple Pay push provisioning</b></summary>

  <Image align="center" src="https://files.readme.io/2ee4b69788486b2038fc51b028c937a0ab977a456657a4d00d24c764a598e860-Apple_Mastercard_Push_Provisioning.png" alt="Mastercard Apple Pay push provisioning" />
</details>

# Tokenizing Pismo card using wallet SDK

You can use the following Pismo endpoints to get the encrypted card data you need for tokenization using the Google Pay, Apple Pay, and Samsung Pay SDKs.

* [Create encrypted data for Google Pay](https://developers.pismo.io/pismo-docs/reference/post-wallet-data)
* [Create encrypted card data for Apple Pay](https://developers.pismo.io/pismo-docs/reference/post-encrypted-applepay-data)
* [Create encrypted card data for Samsung Pay](https://developers.pismo.io/pismo-docs/reference/post-wallet-data-samsung)

# Token lifecyle

Pismo uses the following card token enums:

* `INACTIVE`—Initial token status during provisioning. Can be activated or deactivated.
* `FAILED`—Token was not provisioned due to error. Cannot be changed.
* `ACTIVE`—Activated token that can be used for transactions. Can be suspended or deactivated.
* `SUSPENDED`—Token is temporarily disabled and cannot be used for transactions. Can be activated or deactivated.
* `DEACTIVATED`—Token is deleted. Cannot be changed.

Token statuses are different from [card statuses](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses). Even if a token is `ACTIVE`, transactions are denied if the card status is `BLOCKED`.

Tokenized transactions are approved when the token is `ACTIVE,` even if the physical card status is `CREATED`. The program parameter `ALLOW_TOKENIZED_TRANSACTION_WITH_CREATED_CARD` controls this.

Pismo offers endpoints for getting token information and performing token operations.. Those endpoints are connected directly to the networks and to wallets so they can update their own information when applicable.

* [Get token information](https://developers.pismo.io/pismo-docs/reference/gettokeninfo)—Get token information given a card ID and token ID.
* [Get card tokens](https://developers.pismo.io/pismo-docs/reference/get-card-token-info)—Get information about a card's tokens.
* [Perform token operation](https://developers.pismo.io/pismo-docs/reference/performtokenop)—Perform token operations such as call center activation, delete token, suspend token and so on.

<details>
  <summary>
    <b>Lifecycle example operation</b>
  </summary>

  <Image align="center" src="https://files.readme.io/91b15b4f5bb2ebd5e4da61af7915edd99cb35ebf5fe4ead075d8340b8bf0344c-Life_cycle.png" alt="Lifecycle example operation" />
</details>

# Identifying a tokenized transaction

To identify a tokenized transaction, you can reference the `token_information` object in the [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event.

# Primary account number (PAN) update

The PAN update feature transfers a card's existing provisioned tokens to a new card when the card is reissued

Pismo provides the following endpoints for this purpose. Note that token transfer is not automatic, you need to call one of these endpoints:

* Card reissue endpoint ([Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue))—set `update_tokens` parameter to `true`.
* PAN update endpoint ([Transfer card tokens to other card](https://developers.pismo.io/pismo-docs/reference/transfertokens))

A [PAN updated ](https://developers.pismo.io/events/docs/cards-tokenization-pan-update-1)event is generated when the transfer with the network has concluded.

During update, Pismo sends the new token PAN information to the network, which can then update its own data and, if necessary, pass it to the wallets.  If an error occurs during notification, Pismo considers the transfer as not being made and a new issuer update request is necessary.

Work with your network to make sure this functionality is available.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/cards/{cardId}/network-tokens/profile` | `post-v1-cards-card-id-network-tokens-profile` | Assign network card profile | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--network-card-profile |
| `POST /v1/cards/{cardId}/network-tokens/{tokenId}` | `performtokenop` | Perform token operation | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--token-lifecycle |
| `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/googlepay` | `post-wallet-data` | Create encrypted card data for Google Pay | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--pre-digitalization |
| `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/applepay` | `post-encrypted-applepay-data` | Create encrypted card data for Apple Pay | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--pre-digitalization |
| `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/samsungpay` | `post-wallet-data-samsung` | Create encrypted card data for Samsung Pay | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--pre-digitalization |
| `GET /v1/cards/{cardId}/network-tokens/{tokenId}` | `gettokeninfo` | Get token information | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--token-lifecycle |
| `GET /v1/cards/{cardId}/network-tokens` | `get-card-token-info` | Get card tokens | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--card-lifecycle |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` | `post-v1-card-reissue` | Reissue card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /v1/cards/{cardId}/network-tokens/pan-update` | `transfertokens` | Transfer card tokens to other card | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--card-lifecycle |

### Operation essentials

- **`POST /v1/cards/{cardId}/network-tokens/profile`** (`post-v1-cards-card-id-network-tokens-profile`): security `BearerAuth`; required parameters `cardId` (path); required body fields `network_card_profile`; response statuses 204, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /v1/cards/{cardId}/network-tokens/{tokenId}`** (`performtokenop`): security `BearerAuth`; required parameters `cardId` (path), `tokenId` (path); required body fields `operation_reason`, `operation_type`; response statuses 200, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/googlepay`** (`post-wallet-data`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/applepay`** (`post-encrypted-applepay-data`): security `BearerAuth`; required parameters `cardId` (path); required body fields `Apple_public_certificate_b64`, `device_type`, `app_version`, `Nonce`, `Nonce_signature`; response statuses 200, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/samsungpay`** (`post-wallet-data-samsung`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`GET /v1/cards/{cardId}/network-tokens/{tokenId}`** (`gettokeninfo`): security `BearerAuth`; required parameters `cardId` (path), `tokenId` (path); required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`GET /v1/cards/{cardId}/network-tokens`** (`get-card-token-info`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue`** (`post-v1-card-reissue`): security `BearerAuth`; required parameters `customerId` (path), `accountId` (path), `cardId` (path); required body fields `reason_id`; response statuses 200, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`, `cards-update-1`.
- **`POST /v1/cards/{cardId}/network-tokens/pan-update`** (`transfertokens`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 202, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events `cards-tokenization-pan-update-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-card-reissue` | `cards-create-1` |
| `transfertokens` | `cards-tokenization-pan-update-1` |
| `post-v1-card-reissue` | `cards-update-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `cards-tokenization-pan-update-1` | cards | 1 | https://developers.pismo.io/events/docs/cards-tokenization-pan-update-1 | 1 | KU-EVT-catalogue-cards |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/card-tokenization-process-and-onboarding.md`: updatedAt 2026-04-22T15:19:46.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/card-tokenization-process-and-onboarding.md` | whole document | https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding | `8967390a01eea7e3…` | 2026-04-22T15:19:46.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-tokenization--card-lifecycle` — API reference: Card issuing - Tokenization — Card lifecycle
- `KU-API-card-issuing-tokenization--network-card-profile` — API reference: Card issuing - Tokenization — Network card profile
- `KU-API-card-issuing-tokenization--pre-digitalization` — API reference: Card issuing - Tokenization — Pre-digitalization
- `KU-API-card-issuing-tokenization--token-lifecycle` — API reference: Card issuing - Tokenization — Token lifecycle
- `KU-CARD-card-lifecycle-and-statuses` — Card lifecycle and statuses
- `KU-CARD-card-network-integration` — Card network integration and certification
- `KU-CARD-card-tokenization-flow-and-events` — Card tokenization flow and events
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
