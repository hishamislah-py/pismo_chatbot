---
ku_id: KU-EVT-vcas-client-webhooks
title: Client webhooks for VCAS
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/vcas-client-webhooks.md
  sha256: 45553a95098f2b5921748d801c3eaffa4ce20499d4468718f33fbcad6a6cfb7f
  url: https://developers.pismo.io/pismo-docs/docs/vcas-client-webhooks
  role: primary_guide
  updated_at: '2026-03-18T15:13:58.000Z'
operations: []
related_kus:
- KU-CARD-visa-consumer-authentication-service-vcas
grouping_rationale: single source page
---

# Client webhooks for VCAS

**KU ID:** `KU-EVT-vcas-client-webhooks` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/vcas-client-webhooks.md`:

> Visa Consumer Authentication Service (VCAS) is a Visa-provided service to support 3-D Secure (3DS), a global protocol designed to help issuers authenticate cardholders during card-not-present transactions, such as e-commerce purchases. Issuers need to implement the following webhooks to support VCAS.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/vcas-client-webhooks.md`: Client webhooks for VCAS; VCAS StepUp; VCAS Initiate Action; VCAS Validate

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/vcas-client-webhooks.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/vcas-client-webhooks · updatedAt: 2026-03-18T15:13:58.000Z

<!-- source:begin path=docs/core-platform/vcas-client-webhooks.md part=0-end -->

# Client webhooks for VCAS

Visa Consumer Authentication Service (VCAS) is a Visa-provided service to support 3-D Secure (3DS), a global protocol designed to help issuers authenticate cardholders during card-not-present transactions, such as e-commerce purchases. Issuers need to implement the following webhooks to support VCAS.

<Image alt="Summary diagram of the workflow for VCAS" align="center" src="https://files.readme.io/3d5a25204804fd9fd79ccf00e2626ecc82fd4293d7eb597cacb8810cd5238f0f-Client_webhooks_for_VCAS_overview-Final.png" />

1—Use case #1—VCAS generates, delivers, and validates the OTP.

2—Use case #2—Issuer generates, delivers, and validates the OTP.

3—Use case #3—VCAS generates, issuer delivers, and VCAS validates the OTP.

\*For more information on VCAS and the three use cases noted, refer to the [Visa Consumer Authentication Service (VCAS)](https://developers.pismo.io/pismo-docs/docs/visa-consumer-authentication-service-vcas) guide.

## VCAS StepUp

Webhook request to issuer to provide authentication method and display text.

If the risk assessment results in a status of **StepUp**, this will determine how the issuer can challenge the cardholder.

<details>
  <summary style={{ fontSize: "18px" }}>
    <b>Webhook specifications</b>
  </summary>

  <details>
    <summary style={{ fontSize: "medium" }}>
      <b>Request fields</b>
    </summary>

    <HTMLBlock>
      {`
      <table>
         <tr style={{ backgroundColor: "lightgrey" }}>
            <th>Field</th>
            <th>Type</th>
            <th>Description</th>
            <th>Req</th>
         </tr>
         <tr>
            <td>
               <code>id</code>
            </td>
            <td>string</td>
            <td>Pismo-generated unique authorization ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td>
               <code>provider</code>
            </td>
            <td>enum<br />string</td>
            <td>Third-party provider name:<br />* <code>VCAS</code></td>
            <td>Y</td>
         </tr>
         <tr>
            <td>
               <code>type</code>
            </td>
            <td>enum<br />string</td>
            <td>Call type:<br />* <code>STEPUP</code></td>
            <td></td>
         </tr>
         <tr style={{ backgroundColor: "beige" }}>
            <td>
               <code>card</code>
            </td>
            <td>object</td>
            <td>Card information object</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>id</code>
               
            </td>
            <td>integer</td>
            <td>Card ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>mode_id</code>
               
            </td>
            <td>integer</td>
            <td>Card mode ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>type</code>
               
            </td>
            <td>enum<br />string</td>
            <td>Card type:<br />* <code>PLASTIC</code><br />* <code>VIRTUAL</code><br />* <code>RECURRING</code><br />* <code>TEMPORARY</code></td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>hash</code>
               
            </td>
            <td>string</td>
            <td>Encrypted PAN using 2048 rsa key and base64 encoded.
               Pismo provides the encrypt/decrypt keys for this field.
            </td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>bin</code>
               
            </td>
            <td>string</td>
            <td>Card Bank Identification Number (BIN). A 6 or 8 digit value</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>last_four_digits</code>
               
            </td>
            <td>string</td>
            <td>Card last 4 PAN digits</td>
            <td>Y</td>
         </tr>
         <tr style={{ backgroundColor: "beige" }}>
            <td>
               <code>account</code>
            </td>
            <td>object</td>
            <td>Account information object</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>id</code>
               
            </td>
            <td>string</td>
            <td>Pismo account ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>document_number</code>
               
            </td>
            <td>string</td>
            <td>Cardholder document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil).</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>email</code>
               
            </td>
            <td>string</td>
            <td>E-mail.</td>
            <td>Y</td>
         </tr>
         <tr style={{ backgroundColor: "beige" }}>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>phones</code>
               
            </td>
            <td>object<br />array</td>
            <td>Phone objects</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "60px" }}>
               
               <code>area_code</code>
               
            </td>
            <td>string</td>
            <td>Phone area code</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "60px" }}>
               
               <code>country_code</code>
               
            </td>
            <td>string</td>
            <td>Phone number country code</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "60px" }}>
               
               <code>number</code>
               
            </td>
            <td>string</td>
            <td>Phone number without area code</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "60px" }}>
               
               <code>type</code>
               
            </td>
            <td>enum<br />string</td>
            <td>Phone type:<br />* <code>mobile</code><br />* <code>commercial</code><br />* <code>residential</code></td>
            <td>Y</td>
         </tr>
         <tr style={{ backgroundColor: "beige" }}>
            <td>
               <code>program</code>
            </td>
            <td>object</td>
            <td>Program information object</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>id</code>
               
            </td>
            <td>integer</td>
            <td>Program ID</td>
            <td>Y</td>
         </tr>
         <tr style={{ backgroundColor: "beige" }}>
            <td>
               <code>customer</code>
            </td>
            <td>object</td>
            <td>Customer information object</td>
            <td>Y</td>
         </tr>
         <tr>
            <td style={{ paddingLeft: "30px" }}>
               
               <code>id</code>
               
            </td>
            <td>integer</td>
            <td>Customer ID</td>
            <td>Y</td>
         </tr>
         <tr style={{ backgroundColor: "beige" }}>
            <td>
               <code>raw_provider</code>
            </td>
            <td>object</td>
            <td>All non-PCI information received from provider. Check provider documentation for details.</td>
            <td>Y</td>
         </tr>
      </table>
      `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample request</summary>

    ```json
    {
      "id": "ff77635e-1cd6-4fda-992d-5ceb71d75644",
      "provider": "VCAS",
      "type": "stepup",
      "card": {
        "id": 869572,
        "mode_id": 102,
        "type": "PLASTIC",
        "hash": "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==",
        "bin": "885692",
        "last_four_digits": "0153"
      },
      "account": {
        "id": 10045896,
        "document_number": "00011122233",
        "phones": [
          {
            "area_code": "31",
            "country_code": "55",
            "number": "998675309",
            "type": "mobile"
          }
        ],
        "email": "ho_lee_smokes@gmail.com"
      },
      "program": {
        "id": 986
      },
      "customer": {
        "id": 867604
      },
      "raw_provider": {
        "ProcessorId": "5723ae630063ac1a9c3ab079",
        "IssuerId": "5723ae630063ac1a9c3ab083",
        "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
        "DSTransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f987",
        "ThreeDSRequestorAuthenticationInd": "01",
        "StepupRequestId": "878f4751-4140-4881-9e4a-003e83524f22",
        "DeviceLocale": "en-US",
        "DeviceUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "MessageVersion": "2.2.0",
        "RDXMessageVersion": "2.2.3",
        "MessageCategory": "01",
        "MerchantInfo": {
          "AcquirerId": "1337",
          "AcquirerCountryCode": "840",
          "MerchantId": "876543210",
          "MerchantName": "Ranier Expeditions",
          "MerchantURL": "https://www.requestor.com",
          "MerchantCategoryCode": "0123",
          "MerchantCountryCode": "840",
          "MerchantAppRedirectURL": "merchantScheme://appName?transID=b2385523-a66c-4907-ac3c-91848e8c0067"
        },
        "TransactionInfo": {
          "TransactionCurrency": "840",
          "Channel": "WEB"
        }
      }
    }
    ```
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Response fields</summary>

    <HTMLBlock>
      {`
      <table>
         <tr style={{ backgroundColor: "lightgrey" }}>
            <th>Field</th>
            <th>Type</th>
            <th>Description</th>
            <th>Req</th>
         </tr>
         <tr style={{ backgroundColor: "beige" }}>
            <td>
               <code>raw_response</code>
            </td>
            <td>object</td>
            <td>Raw response to VCAS StepUp request, according with <a href="https://vcasdocs.cardinalcommerce.com/rdx/reference/stepup-biometric" target="_blank">VCAS documentation</a></td>
            <td>Y</td>
         </tr>
      </table>
      `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample response</summary>

    ```json
    {
        "raw_response": {
            "ProcessorId": "5723ae630063ac1a9c3ab07976",
            "IssuerId": "5723ae630063ac1a9c3ab080",
            "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
            "StepupRequestId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
            "StepupType": "OTPEMAIL",
            "Language": "en-US",
            "Status": "SUCCESS",
            "RiskIndicator": "string",
            "Credentials": [
                {
                    "Id": "d94fd3fd-bef1-49cb-88ab-a6841261cea9",
                    "Type": "OTPEMAIL",
                    "Text": "jales@pismo.io"
                }
            ],
            "Reason": {
                "ReasonCode": "string",
                "ReasonDescription": "string"
            },
            "Error": {
                "ReferenceNumber": "string",
                "ReasonDescription": "string",
                "Description": "string",
                "Message": "string"
            },
            "WhyInfo": {
                "Label": "string",
                "Text": "string"
            }
        }
    }
    ```
  </details>
</details>

## VCAS Initiate Action

Webhook to notify issuer to take action, such as generating a verification code.

The **Initiate Action** call takes place once the method of StepUp authentication is identified. The objective of this endpoint is to send the cardholder notification, so the cardholder can be aware of the authentication.

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Webhook specifications</summary>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Request fields</summary>

    <HTMLBlock>
      {`
      <table>
         <tr style="background-color:lightgrey">
            <th>Field</th>
            <th>Type</th>
            <th>Description</th>
            <th>Req</th>
         </tr>
         <tr>
            <td>
               <code>id</code>
            </td>
            <td>string</td>
            <td>Pismo-generated unique authorization ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td>
               <code>provider</code>
            </td>
            <td>enum<br>string</td>
            <td>Third-party provider name:<br>* <code>VCAS</code></td>
            <td>Y</td>
         </tr>
         <tr>
            <td>
               <code>type</code>
            </td>
            <td>enum<br>string</td>
            <td>Call type:<br>* <code>INITIATE_ACTION_CALL</code></td>
            <td></td>
         </tr>
         <tr  style="background-color:beige">
            <td>
               <code>card</code>
            </td>
            <td>object</td>
            <td>Card information object</td>
            <td>Y</td>
         </tr>
         <tr >
            <td style="padding-left:30px">
               
               <code>id</code>
               
            </td>
            <td>integer</td>
            <td>Card ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td  style="padding-left:30px">
               
               <code>mode_id</code>
               
            </td>
            <td>integer</td>
            <td>Card mode ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td  style="padding-left:30px">
               
               <code>type</code>
               
            </td>
            <td>enum<br>string</td>
            <td>Card type:<br>* <code>PLASTIC</code><br>* <code>VIRTUAL</code><br>* <code>RECURRING</code><br>* <code>TEMPORARY</code></td>
            <td>Y</td>
         </tr>
         <tr >
            <td style="padding-left:30px">
               
               <code>hash</code>
               
            </td>
            <td>string</td>
            <td>Encrypted PAN using 2048 rsa key and base64 encoded.
               Pismo provides the encryt/decrypt keys for this field.
            </td>
            <td>Y</td>
         </tr>
         <tr >
            <td style="padding-left:30px">
               
               <code>bin</code>
               
            </td>
            <td>string</td>
            <td>Card Bank Identification Number (BIN). A 6 or 8 digit value</td>
            <td>Y</td>
         </tr>
         <tr >
            <td style="padding-left:30px">
               
               <code>last_four_digits</code>
               
            </td>
            <td>string</td>
            <td>Card last 4 PAN digits</td>
            <td>Y</td>
         </tr>
            <tr  style="background-color:beige">
            <td>
               <code>account</code>
            </td>
            <td>object</td>
            <td>Account information object</td>
            <td>Y</td>
         </tr>
         <tr >
            <td style="padding-left:30px">
               
               <code>id</code>
               
            </td>
            <td>string</td>
            <td>Pismo account ID</td>
            <td>Y</td>
         </tr>
            <tr >
            <td style="padding-left:30px">
               
               <code>document_number</code>
               
            </td>
            <td>string</td>
            <td>Cardholder document number. A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil).</td>
            <td>Y</td>
         </tr>
          <tr >
            <td style="padding-left:30px">
               
               <code>email</code>
               
            </td>
            <td>string</td>
            <td>E-mail.</td>
            <td>Y</td>
         </tr>
             <tr style=" background-color:beige" >
            <td style="padding-left:30px">
               
               <code>phones</code>
               
            </td>
            <td>object<br>array</td>
            <td>Phone objects</td>
            <td>Y</td>
         </tr>
          <tr >
            <td style="padding-left:60px">
               
               <code>area_code</code>
               
            </td>
            <td>string</td>
            <td>Phone area code</td>
            <td>Y</td>
         </tr>
             <tr >
            <td style="padding-left:60px">
               
               <code>country_code</code>
               
            </td>
            <td>string</td>
            <td>Phone number country code</td>
            <td>Y</td>
         </tr>
             <tr >
            <td style="padding-left:60px">
               
               <code>number</code>
               
            </td>
            <td>string</td>
            <td>Phone number without area code</td>
            <td>Y</td>
         </tr>
             <tr >
            <td style="padding-left:60px">
               
               <code>type</code>
               
            </td>
            <td>enum<br>string</td>
            <td>Phone type:<br>* <code>mobile</code><br>* <code>commercial</code><br>* <code>residential</code></td>
            <td>Y</td>
         </tr>
            <tr  style="background-color:beige">
            <td>
               <code>program</code>
            </td>
            <td>object</td>
            <td>Program information object</td>
            <td>Y</td>
         </tr>
          <tr>
            <td style="padding-left:30px">
               
               <code>id</code>
               
            </td>
            <td>integer</td>
            <td>Program ID</td>
            <td>Y</td>
         </tr>
               <tr  style="background-color:beige">
            <td>
               <code>customer</code>
            </td>
            <td>object</td>
            <td>Customer information object</td>
            <td>Y</td>
         </tr>
          <tr>
            <td style="padding-left:30px">
               
               <code>id</code>
               
            </td>
            <td>integer</td>
            <td>Customer ID</td>
            <td>Y</td>
         </tr>
               <tr  style="background-color:beige">
            <td>
               <code>raw_provider</code>
            </td>
            <td>object</td>
            <td>All non-PCI information received from provider. Check provider documentation for details.</td>
            <td>Y</td>
         </tr>

      </table>
      `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample request</summary>

    ```json
    {
      "id": "ff77635e-1cd6-4fda-992d-5ceb71d75644",
      "provider": "VCAS",
      "type": "initiate_action",
      "card": {
        "id": 869572,
        "mode_id": 102,
        "type": "PLASTIC",
        "hash": "WEPvOQuZvjfYEd0iBmr43bhWyOsylIsW95ebYrLD89App2iEq9IizP+8w73pxKQ4mI47EdhzYHF9RfXjrBOyug==",
        "bin": "885692",
        "last_four_digits": "0153"
      },
      "account": {
        "id": 10045896,
        "document_number": "00011122233",
        "phones": [
          {
            "area_code": "31",
            "country_code": "55",
            "number": "998675309",
            "type": "mobile"
          }
        ],
        "email": "ho_lee_smokes@gmail.com"
      },
      "program": {
        "id": 986
      },
      "customer": {
        "id": 867604
      },
      "raw_provider": {
        "ProcessorId": "5723ae630063ac1a9c3ab079",
        "IssuerId": "5723ae630063ac1a9c3ab083",
        "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
        "DSTransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f987",
        "ThreeDSRequestorAuthenticationInd": "01",
        "StepupRequestId": "878f4751-4140-4881-9e4a-003e83524f22",
        "DeviceLocale": "en-US",
        "DeviceUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "MessageVersion": "2.2.0",
        "RDXMessageVersion": "2.2.3",
        "MessageCategory": "01",
        "MerchantInfo": {
          "AcquirerId": "1337",
          "AcquirerCountryCode": "840",
          "MerchantId": "876543210",
          "MerchantName": "Ranier Expeditions",
          "MerchantURL": "https://www.requestor.com",
          "MerchantCategoryCode": "0123",
          "MerchantCountryCode": "840",
          "MerchantAppRedirectURL": "merchantScheme://appName?transID=b2385523-a66c-4907-ac3c-91848e8c0067"
        },
        "TransactionInfo": {
          "TransactionCurrency": "840",
          "Channel": "WEB"
        }
      }
    }
    ```
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Response fields</summary>

    <HTMLBlock>
      {`
      <table>
         <tr style="background-color:lightgrey">
            <th>Field</th>
            <th>Type</th>
            <th>Description</th>
            <th>Req</th>
         </tr>
         <tr style="background-color:beige">
            <td>
               <code>raw_response</code>
            </td>
            <td>object</td>
            <td>Raw response to VCAS initiate action request, according with <a href="https://vcasdocs.cardinalcommerce.com/rdx/reference/initiateaction-otp" target="_blank">VCAS documentation</a></td>
            <td>Y</td>
         </tr>
      </table>
      `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample response</summary>

    ```json

    {
      "raw_response": {
        "ProcessorId": "7723ae630063ac1a9c3ab07976",
        "IssuerId": "5723ae630063ac1a9c3ab080",
        "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
        "StepupRequestId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
        "StepupType": "OTP",
        "Language": "string",
        "Status": "SUCCESS",
        "TransStatusReason": "string",
        "RiskIndicator": "string",
        "Credentials": [
          {
            "Id": "d94fd3fd-bef1-49cb-88ab-a6841261cea9",
            "Type": "OTPEMAIL",
            "Text": "******@cardinalcommerce.com"
          }
        ],
        "Reason": {
          "ReasonCode": "string",
          "ReasonDescription": "string"
        },
        "Error": {
          "ReferenceNumber": "string",
          "ReasonDescription": "string",
          "Description": "string",
          "Message": "string"
        }
      }
    }
    ```
  </details>
</details>

## VCAS Validate

Webhook request to validate the verification code.

In the case of the authentication method, the **Validate** call is used to send the OTP the cardholder entered into the **VCAS Validate** screen.

<details>
  <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Webhook specifications</summary>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Request fields</summary>

    <HTMLBlock>
      {`
      <table>
         <tr style="background-color:lightgrey">
            <th>Field</th>
            <th>Type</th>
            <th>Description</th>
            <th>Req</th>
         </tr>
         <tr>
            <td>
               <code>id</code>
            </td>
            <td>string</td>
            <td>Pismo-generated unique authorization ID</td>
            <td>Y</td>
         </tr>
         <tr>
            <td>
               <code>provider</code>
            </td>
            <td>enum<br>string</td>
            <td>Third-party provider name:<br>* <code>VCAS</code></td>
            <td>Y</td>
         </tr>
         <tr>
            <td>
               <code>type</code>
            </td>
            <td>enum<br>string</td>
            <td>Call type:<br>* <code>VALIDATE</code></td>
            <td></td>
        </tr>
            <tr  style="background-color:beige">
            <td>
               <code>raw_provider</code>
            </td>
            <td>object</td>
            <td>All non-PCI information received from provider. Check provider documentation for details.</td>
            <td>Y</td>
         </tr>

      </table>
      `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample request</summary>

    ```json
    {
      "id": "ff77635e-1cd6-4fda-992d-5ceb71d75644",
      "provider": "VCAS",
      "type": "validate",
      "raw_provider": {
        "ProcessorId": "5723ae630063ac1a9c3ab079",
        "IssuerId": "5723ae630063ac1a9c3ab481",
        "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
        "DSTransactionId": "521fa021-4791-4579-a3e9-76de87c219c0",
        "StepupRequestId": "878f4751-4140-4881-9e4a-003e83524f22",
        "MessageVersion": "2.2.0",
        "RDXMessageVersion": "2.2.3"
      }
    }
    ```
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Response fields</summary>

    <HTMLBlock>
      {`
      <table>
         <tr style="background-color:lightgrey">
            <th>Field</th>
            <th>Type</th>
            <th>Description</th>
            <th>Req</th>
         </tr>
         <tr style="background-color:beige">
            <td>
               <code>raw_response</code>
            </td>
            <td>object</td>
            <td>Raw response to VCAS initiate action request, according with <a href="https://vcasdocs.cardinalcommerce.com/rdx/reference/validate-otp" target="_blank">VCAS documentation</a></td>
            <td>Y</td>
         </tr>
      </table>
      `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{ fontSize: "medium", fontWeight: "bold" }}>Sample response</summary>

    ```json

    {
      "raw_response": {
        "ProcessorId": "5723ae630063ac1a9c3ab079",
        "IssuerId": "5723ae630063ac1a9c3ab671",
        "TransactionId": "00ec043e-40b5-4ce4-95c2-9e83b644f412",
        "StepupRequestId": "00ec043e-40b5-4ce4-95c2-9e83b644f618",
        "Language": "string",
        "CredentialId": "string",
        "Status": "SUCCESS",
        "TransStatusReason": "string",
        "RiskIndicator": "string",
        "Reason": {
          "ReasonCode": "string",
          "ReasonDescription": "string"
        },
        "Error": {
          "ReferenceNumber": "string",
          "ReasonDescription": "string",
          "Description": "string",
          "Message": "string"
        },
        "RReqOverrides": {
          "AuthenticationMethod": "SMS_OTP",
          "TransStatusReason": "CARD_AUTH_FAILED",
          "AuthenticationAttempts": "string",
          "CustomerCancel": true
        }
      }
    ```
  </details>
</details>
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/vcas-client-webhooks.md`: updatedAt 2026-03-18T15:13:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/vcas-client-webhooks.md` | whole document | https://developers.pismo.io/pismo-docs/docs/vcas-client-webhooks | `45553a95098f2b59…` | 2026-03-18T15:13:58.000Z |

## Related knowledge units

- `KU-CARD-visa-consumer-authentication-service-vcas` — Visa Consumer Authentication Service (VCAS)
