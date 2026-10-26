---
ku_id: KU-GS-get-started-with-pismo-apis
title: Get started with Pismo APIs
category: getting_started
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/api-get-started/get-started-with-pismo-apis.md
  sha256: ead0a77603ae887fb3e2924eaa4035d21d5e28bc6d696408066bdeff63bd5710
  url: https://developers.pismo.io/pismo-docs/reference/get-started-with-pismo-apis
  role: primary_guide
  updated_at: '2026-08-31T16:06:27.000Z'
operations:
- CreateProgramBasedOnTemplate
- PostAccountsV2
- createMerchant
- delinquent-account-closure-post
- get-v1-org
- getLoanProductV2
- list-timeline-events
- post-acquisitions-v3-s2s-applications
- post-hierarchies
- post-passport-v1-oauth2-token
- post-pix-out-transfer
- post-v2-card
related_kus:
- KU-API-banking-transaction-banking--hierarchies
- KU-API-card-issuing-cards--cards
- KU-API-core-platform-accounts--accounts
- KU-API-data-and-reporting-timeline--timeline
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-lending--loan-products
- KU-API-migrations--account-migration
- KU-API-platform-authentication--authentication
- KU-API-platform-setup-organizations--orgs
- KU-API-platform-setup-programs--programs-part-01
- KU-API-revolving-credit-delinquent-account--delinquent-account-closure
- KU-API-seller-management-merchants--merchant
- KU-AUTH-authentication-methods
- KU-EVT-catalogue-cards
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-merchants
- KU-EVT-catalogue-migration
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
- KU-GS-environments
grouping_rationale: single source page
---

# Get started with Pismo APIs

**KU ID:** `KU-GS-get-started-with-pismo-apis` · **Category:** Getting started · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/api-get-started/get-started-with-pismo-apis.md`:

> Integrate Pismo solutions with your applications and configure them according to your specific requirements using Pismo's 700+ integration endpoints. The API reference describes these endpoints and how to structure your API requests.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/api-get-started/get-started-with-pismo-apis.md`: Get started with Pismo APIs; Endpoints at a glance; Endpoint description; Recent requests; Parameters; Path parameters; Query parameters; Body parameters; Metadata; Headers; Responses; Interactive console

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 12 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/api-get-started/get-started-with-pismo-apis.md`

Source URL: https://developers.pismo.io/pismo-docs/reference/get-started-with-pismo-apis · updatedAt: 2026-08-31T16:06:27.000Z

<!-- source:begin path=docs/api-get-started/get-started-with-pismo-apis.md part=0-end -->

# Get started with Pismo APIs

Integrate Pismo solutions with your applications and configure them according to your specific requirements using Pismo's 700+ integration endpoints. The API reference describes these endpoints and how to structure your API requests.

Endpoints in the API reference are grouped into the following high-level sections:

* [Platform authentication](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token)
* [Platform setup](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate)
* [Core platform](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)
* [Banking](https://developers.pismo.io/pismo-docs/reference/post-hierarchies)
* [Instant payments](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer)
* [Card issuing](https://developers.pismo.io/pismo-docs/reference/post-v2-card)
* [Revolving credit](https://developers.pismo.io/pismo-docs/reference/delinquent-account-closure-post)
* [Data and reporting](https://developers.pismo.io/pismo-docs/reference/list-timeline-events)
* [Seller management](https://developers.pismo.io/pismo-docs/reference/createmerchant)
* [Migrations](https://developers.pismo.io/pismo-docs/reference/postaccountsv2)
* [Lending](https://developers.pismo.io/pismo-docs/reference/getloanproductv2)

> 📘 Endpoint search
>
> To find a specific endpoint quickly, you can use the **JUMP TO** search field.
>
> <Image align="center" alt="gif showing how to use the JUMP TO search feature" border={true} src="https://files.readme.io/7117ee68e71a05bc9ffce40e7207cec1dde8bfc8362a8805c1379ba3cf018da3-create-merchant.gif" className="border" />

# Endpoints at a glance

An API endpoint is a specific, addressable URL that points to a resource on the API server. It defines where a request is sent and what operation the API performs on the resource.

Refer to the following figure for an overview of a typical endpoint page in the Developers Portal.

<Image align="center" alt="screenshot showing a typical API endpoint page in the Developers Portal" border={true} src="https://files.readme.io/ee83f1c0e07a9df8a4acfd2cfd78a8765ee637d477c1c04cedcb1b6022f80095-endpoint-page-with-callouts-v2.png" className="border" />

| Key | Item                 | Description                                                                                                |
| :-- | :------------------- | :--------------------------------------------------------------------------------------------------------- |
| 1   | Endpoint description | Defines the endpoint and describes the action you can do with it                                           |
| 2   | Recent requests      | Lists the most recent requests you sent through the interactive console                                    |
| 3   | Parameters           | Lists the parameters accepted by the endpoint                                                              |
| 4   | Headers              | Lists the headers accepted by the endpoint                                                                 |
| 5   | Responses            | Lists the response schemas for all possible response types returned by the API for a particular endpoint   |
| 6   | Interactive console  | Provides a dedicated, built-in tool for sending and testing API requests from within the Developers Portal |

To help you navigate the API reference, the following sections describe the standard elements on a typical endpoint page in the Developers Portal and how to build and test API requests. This overview is intended for both complete beginners and those who need a quick refresher on general and Pismo-specific API standards.

## Endpoint description

The endpoint description defines the endpoint and describes the action you can do with it.

<Image align="center" alt="screenshot showing a typical endpoint description, with callouts" border={true} src="https://files.readme.io/2d8df04b49e851e93920c42aecf27f54c24e406b99997e2b80b8e72c6be5a48c-endpoint-description-with-callouts-v2.png" className="border" />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Item
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        Endpoint name
      </td>

      <td>
        Summarizes the action done by the endpoint, for example, **Create exchange rate**
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        HTTP method
      </td>

      <td>
        Defines the type of request you are making

        <ul><li><b>GET</b>: retrieve information</li><li><b>POST</b>: create a new entry</li><li><b>PATCH</b>: update a specific part of a resource</li><li><b>PUT</b>: replace an entire resource with new information</li><li><b>DELETE</b>: remove a resource</li></ul>
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        Endpoint URL
      </td>

      <td>
        Points to the resource where the action is done:

        `https://sandbox.pismolabs.io/rates/v1/exchange-rates`

        If an endpoint accepts a path parameter, the URL includes a placeholder:

        `https://sandbox.pismolabs.io/accounts/v2/customers/{customerId}`
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        Endpoint overview
      </td>

      <td>
        Describes the endpoint

        Make sure you read the overview carefully. It contains important information about prerequisites, endpoint-specific configurations, warnings, and next steps. For example, some endpoints require a specific authentication token type or environment.
      </td>
    </tr>
  </tbody>
</Table>

## Recent requests

The **Recent Requests** table lists the most recent requests you sent through the interactive console.

<Image align="center" alt="screenshot showing a typical Recent Requests table, with callouts" border={true} src="https://files.readme.io/26532a357496eb4d357c0703c476169b6d60986fed1225f48c31b8dcdb8f82dd-recent-requests-callouts.png" className="border" />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Item
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        **TIME** column
      </td>

      <td>
        Indicates how long ago you sent a request

        To view the exact date and time, hover over the request's **TIME** entry.
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        **STATUS** column
      </td>

      <td>
        Indicates the status code of the response received from the API

        For more information, refer to [Responses](#responses).
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        **USER AGENT** column
      </td>

      <td>
        Identifies the user who sent the request. For requests sent through the interactive console, this value is always **Try it!**
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        **INSPECT REQUEST** button
      </td>

      <td>
        Reloads the interactive console with the specific inputs used for the selected request
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        Monthly request log
      </td>

      <td>
        Shows the number of requests you sent to the endpoint in a four-week running period

        Successful requests are shown in green and failed requests are shown in red
      </td>
    </tr>
  </tbody>
</Table>

## Parameters

Parameters are inputs included in an API request that provide specific information or instructions for the API to process.

In Pismo's API reference, parameters are described with the following information:

* Name
* Data type
* If the parameter is required or optional
* Minimum and maximum value constraints, if applicable
* Description
* Example values

Pismo endpoints use the following three parameter types common to REST APIs:

* [Path parameters](#path-parameters)
* [Query parameters](#query-parameters)
* [Body parameters](#body-parameters)

### Path parameters

Path parameters identify a specific resource and are included as part of the endpoint URL. For endpoints that accept path parameters, you must always include the path parameters in the request.

<Image align="center" alt="screenshot showing a typical path parameter section" border={true} src="https://files.readme.io/686d715c77d2ab329ce036ac821acc3879456e1aea5461144fa9578fe3a658ae-path-parameters.png" className="border" />

For example, in `https://sandbox.pismolabs.io/accounts/v2/customers/{customerId}`, **\{customerId}** is a placeholder for a real customer ID value. When you replace the placeholder with a customer ID, the URL points to the customer resource associated with the customer ID you entered.

### Query parameters

Query parameters filter the information returned in an API response. They're appended to the end of the endpoint URL, represented by a question mark (**?**).

<Image align="center" alt="screenshot showing a typical query parameters section" border={true} src="https://files.readme.io/f0cf2c3c98ddb095a4c6ffd008d4c892b8905f4d0874540dddd020be82ad8be6-query-parameters.png" className="border" />

For example, in `https://sandbox.pismolabs.io/acquisitions/v2/programs/{programId}/channels?perPage=10`, **perPage=10** filters the response to list only 10 items per page.

> 📘 Multiple filters
>
> You can include more than one query parameter in your request by separating each query parameter with an ampersand (**&**).
>
> `https://sandbox.pismolabs.io/acquisitions/v2/programs/{programId}/channels?page=1&perPage=10`

### Body parameters

Body parameters are inputs included in the body of an API request. They provide the information the API needs to create or update a resource.

<Image align="center" alt="screenshot showing a typical body parameter section" border={true} src="https://files.readme.io/a72be93953caced4a8bc16df08676c60695e876b1e674d025f9f75c73d912425-body-parameters.png" className="border" />

The structure and format of the request body depend on the programming language you use to send the request. Refer to the following code extract for an example of a typical request body in cURL, for the creation of a new account phone number.

```curl
     --data '
{
  "type": "RESIDENTIAL",
  "country_code": 55,
  "number": "11912345678",
  "active": true,
  "area_code": 11,
  "extension": "ext. 9"
}
'
```

The interactive console includes a language selector, so you can view request syntax in a variety of common languages. For more information, refer to [Interactive console](#interactive-console).

## Metadata

<Callout icon="🚧" theme="warn">
  **Important: Metadata fields — Data Privacy Notice**

  The metadata parameters available across Pismo APIs are designed for operational, non-sensitive data only (e.g., internal reference IDs, workflow tags, operational flags).

  Clients **MUST NOT** use metadata fields to send:

  * Personally Identifiable Information (PII)
  * Payment Card Industry (PCI) data
  * Sensitive Personal Information (SPII)
  * Any regulated or sensitive information
</Callout>

For handling sensitive data, use the specific, purpose-built API parameters that have appropriate security controls and data governance safeguards. Pismo does not validate or filter the content of metadata fields. Any sensitive data sent through these fields is the client's responsibility and may not be protected by the same security controls applied to designated sensitive-data fields.

## Headers

Headers are additional metadata included and sent with your request. They define how a request is processed, specify the request and response formats, and control access. Like parameters, each header listed in the **Headers** section includes useful information describing the header and its purpose.

<Image align="center" alt="screenshot showing a typical headers section" border={true} src="https://files.readme.io/1f958b5a91280b9d511ac39254e2ae1285480cf4bfaa0b8e7034b6d9a576174a-headers.png" className="border" />

You must include the following headers with all Pismo API requests:

* **accept: application/json**, which indicates the preferred API response format.\
  In most cases, the **accept** header is already included in the interactive console by default and the field is not present in the **Headers** section.
* **content-type: application/json**, which indicates the request body format.\
  In most cases, the **content-type** header is already included in the interactive console by default and the field is not present in the **Headers** section.
* **authorization: Bearer\<access\_token>**, which stores your authentication token and checks the request is sent from an authorized user or system.

> 📘 Authentication scheme
>
> Pismo API requests are authenticated using the **Bearer** authentication scheme. When you send a request, make sure you format the authorization header correctly.
>
> `authorization: Bearer <your_bearer_token>`
>
> If you don't format the authorization header correctly, you'll get an error response.
>
> For more information, refer to the following guides:
>
> * [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials)
> * [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid)
> * [Authentication with OAuth2](https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2)

> 📘 Endpoint-specific headers
>
> Some endpoints accept additional headers specific to the endpoint. The purpose of these headers is described in the **Headers** section for each header.

## Responses

All API requests return a response. A response informs you if your request was successful and returns data relevant to the outcome of the request. The **Responses** section lists structured schemas for the possible responses returned by the API for a particular endpoint.

<Image align="center" alt="screenshot showing a typical responses section" border={true} src="https://files.readme.io/f655bf5929fe740c7ef42ca5069dc6d6c48e15f612891787c77782ea602d243e-responses.png" className="border" />

A response schema defines the expected response and includes the following information:

* An HTTP status code
* A short summary
* Details of each attribute included in the response along with a short description

The HTTP status code is a standardized numerical code that defines the general classification of a response and is included with all API responses. Refer to the following table for an overview of the status codes used in REST APIs.

| Status code | Description                                                                                                                                   |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| 1xx         | **Informational**: represents a temporary, non-final response that indicates the request is received and processing.                          |
| 2xx         | **Success**: the request was successfully received, validated, and processed by the server.                                                   |
| 3xx         | **Redirection**: the client must take additional action to complete the request.                                                              |
| 4xx         | **Client error**: the request failed because the client sent invalid, incomplete, or unauthorized input that the server is unable to process. |
| 5xx         | **Server error**: the request failed due to an error on the server.                                                                           |

For more information on API responses and response examples, refer to [Interactive console](#interactive-console).

## Interactive console

Use the interactive console to test requests in a sandbox environment directly from the Developers Portal.

<Image align="center" alt="screenshot showing a typical interactive console" border={true} src="https://files.readme.io/0ac0fa564547a5287767e2a1a92f0ee75cdb388fc218f5ca5ffd4d2fce985865-interactive-console-with-callouts.png" className="border" />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
      </th>

      <th>
        Item
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        **LANGUAGE** selector
      </td>

      <td>
        Specifies the programming language shown in the code editor

        Select the more options icon (![](https://files.readme.io/d6c2250bdbf683b8f6373eacf8d695896020415211b25d2d59785462d847db8d-more-items-vertical.svg)) for a list of additional language options.
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        **CREDENTIALS** field
      </td>

      <td>
        Accepts and stores your authentication token

        The **CREDENTIALS** field is not always present. Depending on the endpoint, an authentication token field is instead included in the **Headers** section.

        For more information, refer to [Headers](#headers).
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        **URL** drop-down
      </td>

      <td>
        Defines the sandbox server where the request is sent

        The **URL** drop-down is only included for endpoints that have server-specific constraints. For example, if you're sending a request that handles cardholder data, you must use the dedicated Payment Card Industry (PCI) server.

        `https://gw-pci.pismolabs.io`

        If the **URL** drop-down is not present on a particular endpoint page, your request is sent to the default `https://sandbox.pismolabs.io` server.

        For more information, refer to [Environments](https://developers.pismo.io/pismo-docs/docs/environments).
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        Code editor
      </td>

      <td>
        Shows the request in your selected programming language

        The code editor updates automatically based on the values you provide in the following sections and fields:

        <ul><li><b>Path Params</b></li><li><b>Query Params</b></li><li><b>Body Params</b></li><li><b>Headers</b></li><li><b>CREDENTIALS</b></li><li><b>URL</b></li></ul>
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        **RESPONSE** pane
      </td>

      <td>
        Displays the response to your request

        The **RESPONSE** pane also provides endpoint-specific examples of successful and failed responses with mock data, showing how a typical real-world example is formatted.
      </td>
    </tr>
  </tbody>
</Table>

To send a request using the interactive console, do the following:

1. Read the endpoint overview and make sure you meet all the prerequisites.
2. Configure the request parameters and headers.
3. From **LANGUAGE**, select a programming language.
4. If applicable, do the following:
   * In **CREDENTIALS**, enter your authentication token.
   * From **URL**, select the server where you want to send the request.
5. Select **Try it!**. The request is sent and the response is displayed in the **RESPONSE** pane.

Refer to the following figure for an overview of the request process, using the [Get organization](https://developers.pismo.io/pismo-docs/reference/get-v1-org) endpoint as an example.

<Image align="center" alt="gif of a request being set in the Developers Portal" border={true} src="https://files.readme.io/e8e0d71a9660cf6d1bfa36f4c7d01bccfdd29dfe6d790c8cb815c24a47337548-get-organization-all-blurred.gif" className="border" />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/oauth2/token` | `post-passport-v1-oauth2-token` | Get OpenID access token | `api-specs/Platform_authentication.yaml` | no | KU-API-platform-authentication--authentication |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /corporate/v1/hierarchies` | `post-hierarchies` | Create hierarchy | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /wallet/v2/cards` | `post-v2-card` | Create card | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /v1/accounts/{account_id}/close` | `delinquent-account-closure-post` | Close delinquent account | `api-specs/Revolving_credit_-_Delinquent_account.yaml` | no | KU-API-revolving-credit-delinquent-account--delinquent-account-closure |
| `GET /timeline/v1/timeline` | `list-timeline-events` | List account timeline events | `api-specs/Data_and_reporting_-_Timeline.yaml` | no | KU-API-data-and-reporting-timeline--timeline |
| `POST /v1/merchants` | `createMerchant` | Create merchant | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant |
| `POST /v2/migrations/accounts` | `PostAccountsV2` | Migrate accounts | `api-specs/Migrations.yaml` | no | KU-API-migrations--account-migration |
| `GET /v2/loan-products/{productId}` | `getLoanProductV2` | Get loan product | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /orgs-core/v1/orgs/{id}` | `get-v1-org` | Get organization | `api-specs/Platform_setup_-_Organizations.yaml` | no | KU-API-platform-setup-organizations--orgs |

### Operation essentials

- **`POST /v1/oauth2/token`** (`post-passport-v1-oauth2-token`): security not declared; required parameters none declared; required body fields `token`; response statuses 201, 401, 500; error codes in examples none; events none listed.
- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /corporate/v1/hierarchies`** (`post-hierarchies`): security `BearerAuth`; required parameters none declared; required body fields `name`, `levels`; response statuses 201, 400, 401, 403, 500; error codes in examples `WHIE0001`, `WHIE0002`, `WHIE0003`, `WHIE0004`, `WHIE0005`, `WHIE0007`, `ECMN9999`; events `corporate-hierarchy-creation-1`.
- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /wallet/v2/cards`** (`post-v2-card`): security `BearerAuth`; required parameters `x-customer-id` (header); required body fields `name`, `type`; response statuses 200, 201, 401, 403, 409, 500; error codes in examples none; events `cards-create-1`.
- **`POST /v1/accounts/{account_id}/close`** (`delinquent-account-closure-post`): security `BearerAuth`; required parameters `account_id` (path); required body fields `tracking_id`; response statuses 202, 400, 409, 500; error codes in examples none; events `delinquent-account-delinquent-account-1`.
- **`GET /timeline/v1/timeline`** (`list-timeline-events`): security `S2SAuthentication`; required parameters none declared; required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /v1/merchants`** (`createMerchant`): security `BearerAuth`; required parameters none declared; required body fields `document_number`, `name`, `email`; response statuses 201, 400, 401, 500; error codes in examples none; events `merchants-merchant-created-1`.
- **`POST /v2/migrations/accounts`** (`PostAccountsV2`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `applicant`; response statuses 202, 400, 500; error codes in examples `MIGR00002`, `MIGR00001`; events `migration-account-incoming-2`, `migration-account-outgoing-2`.
- **`GET /v2/loan-products/{productId}`** (`getLoanProductV2`): security `BearerAuth`; required parameters `productId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ELND0002`, `ELND0005`, `ELND0005`, `ELND0001`; events none listed.
- **`GET /orgs-core/v1/orgs/{id}`** (`get-v1-org`): security `S2SAuthentication`; required parameters `id` (path), `x-tenant` (header); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples `EOA0030`, `EOA0035`, `EOA0100`, `EOA0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v2-card` | `cards-create-1` |
| `post-hierarchies` | `corporate-hierarchy-creation-1` |
| `delinquent-account-closure-post` | `delinquent-account-delinquent-account-1` |
| `createMerchant` | `merchants-merchant-created-1` |
| `PostAccountsV2` | `migration-account-incoming-2` |
| `PostAccountsV2` | `migration-account-outgoing-2` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/api-get-started/get-started-with-pismo-apis.md`: updatedAt 2026-08-31T16:06:27.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/api-get-started/get-started-with-pismo-apis.md` | whole document | https://developers.pismo.io/pismo-docs/reference/get-started-with-pismo-apis | `ead0a77603ae887f…` | 2026-08-31T16:06:27.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-data-and-reporting-timeline--timeline` — API reference: Data and reporting - Timeline — Timeline
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-migrations--account-migration` — API reference: Migrations — Account migration
- `KU-API-platform-authentication--authentication` — API reference: Platform authentication — Authentication
- `KU-API-platform-setup-organizations--orgs` — API reference: Platform setup - Organizations — Orgs
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-revolving-credit-delinquent-account--delinquent-account-closure` — API reference: Revolving credit - Delinquent account — Delinquent account closure
- `KU-API-seller-management-merchants--merchant` — API reference: Seller management - Merchants — Merchant
- `KU-AUTH-authentication-methods` — API authentication methods: OAuth2, OpenID Connect, client credentials, third-party authentication and access keys
- `KU-EVT-catalogue-cards` — Event catalogue: cards
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-EVT-catalogue-migration` — Event catalogue: migration
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-GS-environments` — Environments
