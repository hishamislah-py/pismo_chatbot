---
ku_id: KU-GS-welcome
title: Get started with the Pismo Developers Portal
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/get-started/welcome.md
  sha256: b5fa63103662055db048a84dfc18bb5800ab83e17417d7ba47e650b06dee870a
  url: https://developers.pismo.io/pismo-docs/docs/welcome
  role: primary_guide
  updated_at: '2026-06-30T14:16:29.000Z'
operations:
- post-passport-v1-oauth2-token
related_kus:
- KU-API-platform-authentication--authentication
- KU-BANK-get-started-building-banking
- KU-CARD-digital-wallets
- KU-CARD-get-started-card-issuing
- KU-CC-get-started-control-center
- KU-CORE-accounts-overview
- KU-EVT-catalogue-overdraft
- KU-EVT-data-events-concepts
- KU-GS-ai-assisted-documentation
- KU-LEND-get-started-lending
- KU-RPT-scheduled-reports
- KU-SELL-get-started-seller-management
- KU-SUP-service-desk-requests
grouping_rationale: single source page
---

# Get started with the Pismo Developers Portal

**KU ID:** `KU-GS-welcome` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/get-started/welcome.md`:

> The Pismo Developers Portal provides comprehensive documentation to help you integrate services from the Pismo platform, Pismo’s cloud-native all-in-one processing platform for banking and payments, into your applications. It brings together detailed product guides, a REST API reference, JSON event schemas, and a monthly changelog, all in one place.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/get-started/welcome.md`: Get started with the Pismo Developers Portal; Who is it for?; Why use it?; How is it organized?; Guides; APIs; Events; Changelog; How do I find what I need?; How do I contact Pismo?

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/get-started/welcome.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/welcome · updatedAt: 2026-06-30T14:16:29.000Z

<!-- source:begin path=docs/get-started/welcome.md part=0-end -->

# Get started with the Pismo Developers Portal

The Pismo Developers Portal provides comprehensive documentation to help you integrate services from the Pismo platform, Pismo’s cloud-native all-in-one processing platform for banking and payments, into your applications. It brings together detailed product guides, a REST API reference, JSON event schemas, and a monthly changelog, all in one place.

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=ynxGR3kliRU" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FynxGR3kliRU%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DynxGR3kliRU%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FynxGR3kliRU%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22800%22%20height%3D%22450%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=ynxGR3kliRU" providerUrl="https://www.youtube.com/" providerName="YouTube" />

# Who is it for?

The Developers Portal supports the following teams and processes:

* **Developers** building integrations using Pismo APIs
* **Solution architects** planning service implementations
* **Technical and operations teams** managing configurations and monitoring platform changes
* **Product teams** exploring the capabilities of the Pismo platform

# Why use it?

The Developers Portal consolidates all technical information required for you to understand and use the Pismo platform, and provides key use cases, including the ability to:

* Access the most up-to-date API reference documentation for all Pismo solutions.
* Learn about Pismo’s offerings, and how to implement them, through comprehensive guides.
* Explore Pismo's data event library and find out how to configure real-time and batch event processing.
* Familiarize yourself with Control Center, Pismo’s interactive user interface for configuring your integrations.
* Track platform updates and service deprecations through the monthly changelog.

# How is it organized?

The Developers Portal is organized into four high-level sections:

* [Guides](#guides)
* [APIs](#apis)
* [Events](#events)
* [Changelog](#changelog)

<Image align="center" alt="screenshot showing the Pismo Developers Portal homepage banner and navbar" border={true} src="https://files.readme.io/6941adc83fb817cdbb63ca84fd8ab80904e4818c3390c4fba6e63cca8dae95c8-developers-portal-home.png" className="border" />

## Guides

The **Guides** section provides comprehensive product documentation, including conceptual overviews and step-by-step guidance, for building your products using the Pismo platform. The guides are organized by [core platform](https://developers.pismo.io/pismo-docs/docs/accounts-overview), [data and reporting](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview), and product solutions.

To learn more about Pismo's main solutions, explore the following guides.

<Cards columns={2}>
  <Card title="Card issuing" href="https://developers.pismo.io/pismo-docs/docs/get-started-building-card-issuing">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="25" fill="none" viewBox="0 0 35 25">
      <path stroke="#FFA945" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 2H3a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2ZM1 8h22" />

      <path stroke="#FFA945" stroke-linecap="round" stroke-width="2" d="M5 15h2m3 0h3.5" />
    </svg>

    Issue and manage a variety of card types, including debit, credit, prepaid, white-label, and private-label cards.
  </Card>

  <Card title="Core banking" href="https://developers.pismo.io/pismo-docs/docs/get-started-building-banking">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="25" fill="none" viewBox="0 0 35 25">
      <path stroke="#FFA945" stroke-width="1.25" d="m2.125 7.238-.586-.036c-.456-.028-.811-.325-.894-.749H.644a.97.97 0 0 1 .387-.985l.134-.075 10.5-4.696h.001a.818.818 0 0 1 .669 0l10.5 4.696c.379.169.61.608.52 1.058v.004c-.088.452-.458.746-.854.746h-.625v1.017c0 .33-.247.549-.5.549H2.625c-.252 0-.5-.22-.5-.55v-.979Zm3.208 3.822v8.347h3.125V11.06h1.75v8.347h3.542V11.06h1.75v8.347h3.126V11.06h1.75v8.308l.354.164.026.017 2.25 1.391c.318.197.432.538.335.834-.1.307-.424.557-.84.557H1.458c-.365 0-.697-.241-.8-.556-.096-.295.018-.637.338-.835h.001l2.25-1.391.157-.098.035-.076a.629.629 0 0 0 .144-.469V11.06h1.75Zm-2.153 8.5c-.003 0-.007 0-.01.002l.012-.004-.002.002Z" />

      <path stroke="#FFA945" stroke-width="2" d="M9.391 11.478v8.554m5.218-8.554v8.554m5.217-8.554v8.554m-15.13-8.554v8.554" />

      <circle cx="12" cy="5" r="2" fill="#FFA945" />
    </svg>

    Integrate your choice of Pismo's banking capabilities, including accounts, balance tracking, interest-bearing products, instant payment, and transaction banking, with your products and services.
  </Card>

  <Card title="Lending" href="https://developers.pismo.io/pismo-docs/docs/get-started-building-lending">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="25" fill="none" viewBox="0 0 35 25">
      <g clip-path="url(#a)">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 0v22m5-18H4.5a3.5 3.5 0 1 0 0 7h5a3.5 3.5 0 1 1 0 7H1" />
      </g>

      <defs>
        <clipPath id="a">
          <path fill="#fff" d="M0 0h35v25H0z" />
        </clipPath>
      </defs>
    </svg>

    Create personal and Buy Now, Pay Later (BNPL) loan products, and configure disbursement and repayment options across the full loan lifecycle.
  </Card>

  <Card title="Digital wallets" href="https://developers.pismo.io/pismo-docs/docs/wallet-overview">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="25" fill="currentColor" viewBox="0 0 35 25">
      <path d="M19.7 5.444h-1.1v-1.11a3.35 3.35 0 0 0-.966-2.358A3.284 3.284 0 0 0 15.3 1h-11c-.875 0-1.715.351-2.333.976A3.35 3.35 0 0 0 1 4.333v13.334c0 .884.348 1.732.967 2.357A3.283 3.283 0 0 0 4.3 21h15.4c.875 0 1.715-.351 2.334-.976A3.35 3.35 0 0 0 23 17.667v-8.89a3.35 3.35 0 0 0-.966-2.356 3.284 3.284 0 0 0-2.334-.977ZM4.3 3.222h11c.292 0 .571.117.778.326.206.208.322.49.322.785v1.111H4.3c-.292 0-.572-.117-.778-.325a1.117 1.117 0 0 1 0-1.571c.206-.209.486-.326.778-.326Zm16.5 11.111h-1.1c-.292 0-.572-.117-.778-.325a1.117 1.117 0 0 1 0-1.571c.206-.209.486-.326.778-.326h1.1v2.222Zm0-4.444h-1.1c-.875 0-1.715.351-2.334.976a3.35 3.35 0 0 0-.966 2.357c0 .884.348 1.732.966 2.357a3.283 3.283 0 0 0 2.334.977h1.1v1.11c0 .295-.116.578-.322.786a1.094 1.094 0 0 1-.778.326H4.3c-.292 0-.572-.117-.778-.326a1.116 1.116 0 0 1-.322-.785V7.477c.353.126.725.19 1.1.19h15.4c.292 0 .572.117.778.325.206.208.322.491.322.786v1.11Z" />
    </svg>

    Tokenize and provision payment cards securely through Pismo's tokenization endpoints for use in digital wallets and token-based payment solutions.
  </Card>

  <Card title="Control Center" href="https://developers.pismo.io/pismo-docs/docs/get-started-building-control-center">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="25" fill="none" viewBox="0 0 35 25">
      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 20h8m-4-4v4m8-18H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2Z" />
    </svg>

    Build and manage your payment and banking programs on the Pismo platform through Control Center's interactive user interface.
  </Card>

  <Card title="Seller management" href="https://developers.pismo.io/pismo-docs/docs/get-started-building-seller-management">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="25" fill="none" viewBox="0 0 35 25">
      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 22a1 1 0 1 0 0-2 1 1 0 0 0 0 2ZM9 22a1 1 0 1 0 0-2 1 1 0 0 0 0 2ZM1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6" />
    </svg>

    Manage online and point-of-sale merchant and marketplace processes.
  </Card>
</Cards>

Use the guides when you need to do the following:

* Understand platform concepts and workflows.
* Learn how to integrate and configure Pismo solutions with your applications.
* Explore domain-specific features before diving into the APIs.

## APIs

The **[APIs](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token)** section contains Pismo’s API reference, an extensive RESTful API library with more than 600 integration endpoints. It's organized by product and functionality.

Each endpoint includes the following common items:

* The endpoint URL
* A description of the endpoint and its purpose
* A list of the accepted parameters
* A list of the accepted headers
* A list of possible responses
* An interactive ‘try it yourself’ console for testing API calls directly, in real time, from the Developers Portal itself

> 📘 Pismo Postman collection
>
> For a more customizable and streamlined approach to testing Pismo APIs, Pismo provides a ready-to-use Postman API collection.
>
> For more information, refer to [Test Pismo APIs with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).

Use this section when you need to do the following:

* Integrate Pismo API endpoints with your applications.
* Understand request and response structures.
* Test API calls using the interactive console.

For more information, refer to [Get started with Pismo APIs](https://developers.pismo.io/pismo-docs/reference/get-started-with-pismo-apis).

## Events

The **[Events](https://developers.pismo.io/events/docs/event-base-main-event)** section is a dedicated space for Pismo data events. The Pismo platform is built on an event‑driven architecture, where data events give you real‑time visibility into what’s happening across your financial operations. Each event represents a specific action, for example, a payment, account update, or settlement, and includes detailed data useful for reporting and analytics.

Data events are delivered in JSON format, and you can choose to receive events in real time or as batch file deliveries, depending on your specific internal data workflows.

<Accordion title="JSON data event schema and message example">
  The following JSON code snippet is an example of a data event schema. It describes the structure of the JSON data event message for the <a href="https://developers.pismo.io/events/docs/overdraft-product-creation-1">creation of an overdraft product</a> and defines the properties of the included attributes.

  ```json
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "title": "Overdraft product created",
      "description": "Create an organization's overdraft product.",
      "required": [
          "product_id",
          "name",
          "interest_plan_id",
          "processing_codes",
          "status",
          "created_at"
      ],
      "properties": {
          "product_id": {
              "type": "string",
              "title": "Product ID",
              "description": "Product ID on the Pismo platform. The ID is in the UUID v4 format.",
              "examples": [
                  "2c336e9d-d04f-4fd0-8f6e-25808f48d70c"
              ]
          },
          "name": {
              "type": "string",
              "title": "Product name",
              "description": "Name of the overdraft product",
              "examples": [
                  "Tax 1 Default"
              ]
          },
          "interest_plan_id": {
              "type": "string",
              "title": "Interest plan ID",
              "description": "Your interest plan ID on the Pismo platform. Displayed in the UUID v4 format.",
              "examples": [
                  "b935acaf-886c-4817-8f7c-c2cc3ce4d509"
              ]
          },
          "processing_codes": {
              "type": "object",
              "title": "Processing codes",
              "description": "Accounting processing codes",
              "required": [
                  "interest_processing_code"
              ],
              "properties": {
                  "interest_processing_code": {
                      "type": "string",
                      "title": "Interest processing code",
                      "description": "Processing code used to identify interest-related transactions such as interest accrual, charging, and reversals on the overdraft balance.",
                      "examples": [
                          "202526"
                      ]
                  }
              }
          },
          "status": {
              "type": "string",
              "title": "Status",
              "description": "Overdraft product status. The status of a new product's status is always `CREATED`.",
              "examples": [
                  "CREATED"
              ]
          },
          "created_at": {
              "type": "string",
              "format": "date-time",
              "title": "Product creation datetime",
              "description": "Overdraft product creation datetime. Represented as an RFC3339 timestamp.",
              "examples": [
                  "2024-01-23T13:26:25"
              ]
          },
          "grace_period": {
              "type": "integer",
              "title": "Grace period",
              "description": "Grace period in days.",
              "examples": [
                  0
              ]
          }
      }
  }
  ```

  And the following is an example of the actual data event message you receive when you create an overdraft product.

  ```json
  {
      "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
      "name": "Tax 1 Default",
      "interest_plan_id": "b935acaf-886c-4817-8f7c-c2cc3ce4d509",
      "processing_codes": {
          "interest_processing_code": "202526"
      },
      "status": "CREATED",
      "created_at": "2024-01-23T13:26:25",
      "grace_period": 0
  }
  ```
</Accordion>

Use this section when you need to do the following:

* Understand the format and structure of data events.
* Validate event-specific data.
* Reference data event schemas for integration with your internal reporting and analytics programs.

For more information, refer to [Data events](https://developers.pismo.io/pismo-docs/docs/event-data) and [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Changelog

The **[Changelog](https://developers.pismo.io/pismo-docs/changelog)** section notifies you about new features, updates, and service deprecations on the Pismo platform, the Developers Portal, and Control Center. It's updated monthly.

Use this section when you need to do the following:

* Track platform changes that might affect your integrations and configurations.
* Plan for upcoming service deprecations.

# How do I find what I need?

The Developers Portal includes a built-in AI assistant called **Ask AI** to help you answer questions about the Pismo platform. For more information, refer to [Get started with Ask AI](https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai).

<Image align="center" alt="gif showcasing the Ask AI feature" border={true} src="https://files.readme.io/9af9c7832cd365ccc449a9ad9150a33c85411a61365f6663189e138562de9b58-ask-ai-example.gif" className="border" />

# How do I contact Pismo?

Pismo is committed to maintaining high-quality, comprehensive documentation, and we welcome your input. To share your feedback, you can do either of the following:

* Open a [Service Desk request](https://developers.pismo.io/pismo-docs/docs/service-desk) and select the **Projects** request type.
* Leave a comment using the **Did this page help you?** feedback widget, located at the bottom of all pages in **Guides** and **APIs**.

<Image align="center" alt="screenshot showing the feedback widget" border={true} src="https://files.readme.io/6e24f052207ce6112529bfdb41f72975921dde99fa800fa13ca2cef874d6c6c5-feedback-widget.png" className="border" />

If you're experiencing issues with the Pismo platform, the Pismo Service Desk is here to help. For more information, refer to [Support](https://developers.pismo.io/pismo-docs/docs/support).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/oauth2/token` | `post-passport-v1-oauth2-token` | Get OpenID access token | `api-specs/Platform_authentication.yaml` | no | KU-API-platform-authentication--authentication |

### Operation essentials

- **`POST /v1/oauth2/token`** (`post-passport-v1-oauth2-token`): security not declared; required parameters none declared; required body fields `token`; response statuses 201, 401, 500; error codes in examples none; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `get-started-with-pismo-apis` | Get started with Pismo APIs | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `overdraft-product-creation-1` | overdraft | 1 | https://developers.pismo.io/events/docs/overdraft-product-creation-1 | 1 | KU-EVT-catalogue-overdraft |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/get-started/welcome.md`: updatedAt 2026-06-30T14:16:29.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `get-started-with-pismo-apis` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/get-started/welcome.md` | whole document | https://developers.pismo.io/pismo-docs/docs/welcome | `b5fa63103662055d…` | 2026-06-30T14:16:29.000Z |

## Related knowledge units

- `KU-API-platform-authentication--authentication` — API reference: Platform authentication — Authentication
- `KU-BANK-get-started-building-banking` — Get started with banking
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-CARD-get-started-card-issuing` — Get started with card issuing
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CORE-accounts-overview` — Accounts
- `KU-EVT-catalogue-overdraft` — Event catalogue: overdraft
- `KU-EVT-data-events-concepts` — Data events: concepts and event-generating APIs
- `KU-GS-ai-assisted-documentation` — AI-assisted documentation: Ask AI and LLM access
- `KU-LEND-get-started-lending` — Get started with lending
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
- `KU-SELL-get-started-seller-management` — Get started with seller management
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
