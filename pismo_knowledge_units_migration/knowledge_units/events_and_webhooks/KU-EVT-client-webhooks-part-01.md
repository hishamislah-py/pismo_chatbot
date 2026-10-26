---
ku_id: KU-EVT-client-webhooks-part-01
title: Client webhooks (part 1 of 14)
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/client-webhooks.md
  sha256: cd35b3bad1d1b22bcca9904923038c09b3581f0196a1afc2f4a7a436effd79f4
  url: https://developers.pismo.io/pismo-docs/docs/client-webhooks
  role: primary_guide
  updated_at: '2026-09-18T17:12:01.000Z'
operations:
- gettokeninfo
- post-authorization
- post-integrated-payments-api-v1-bankslips-cashout
- post-integrated-payments-api-v1-bankslips-pay
- post-payments
- post-payments-v1-installments
- post-payments-v1-payments
- post-pix-out-transfer
- post-pix-reversal
- post-transfers
related_kus:
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--transfer
- KU-API-card-issuing-tokenization--token-lifecycle
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payments
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-CARD-card-tokenization-flow-and-events
- KU-CARD-card-tokenization-process-and-onboarding
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-integrated
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
- KU-EVT-verifying-webhook-requests
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 1 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-01` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> Webhooks are user-defined HTTP callbacks that customers can code to interact with the Pismo platform during certain operations. Client webhooks should be registered with Pismo during setup. Talk to your Pismo representative about getting these implemented.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: Client webhooks; Client anti-fraud webhook for card tokenization; Client anti-fraud webhook for banking transaction

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 1–837 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=0-837 -->

# Client webhooks

Webhooks are user-defined HTTP callbacks that customers can code to interact with the Pismo platform during certain operations. Client webhooks should be registered with Pismo during setup. Talk to your Pismo representative about getting these implemented.

> 📘 Pismo webhook security
>
> For information on webhook security, refer to [Verifying webhook requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests).

# Client anti-fraud webhook for card tokenization

As a card issuer, you can provide your own anti-fraud card verification via a webhook that Pismo calls during the tokenization process. If you don't provide one, Pismo uses a default anti-fraud method. You need to configure this webhook with your Pismo representative.

You can:

* Approve a card
* Not approve a card
* Ask Pismo to prompt the cardholder for further identity and verification in the form of  SMS, phone call,  or app.

For more information, refer to [Card tokenization process and onboarding](https://developers.pismo.io/pismo-docs/docs/card-tokenization-process-and-onboarding) and [Card tokenization flow and events](https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events).

<details>
  <summary style={{fontSize: "18px"}}><b>Webhook specifications</b></summary>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Request fields</summary>

    <Table align={["left","left","left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Field
          </th>

          <th style={{ textAlign: "left" }}>
            Type
          </th>

          <th style={{ textAlign: "left" }}>
            Description
          </th>

          <th style={{ textAlign: "left" }}>
            Required
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            `custom_codes`
          </td>

          <td style={{ textAlign: "left" }}>
            string array
          </td>

          <td style={{ textAlign: "left" }}>
            Card status validation codes indicating Pismo's findings. Issuer can still approve. Note that custom codes are listed elsewhere, but not all apply to this webhook.

            Refer to Custom codes table below.
          </td>

          <td style={{ textAlign: "left" }}>
            No
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `token_id`
          </td>

          <td style={{ textAlign: "left" }}>
            number
          </td>

          <td style={{ textAlign: "left" }}>
            Pismo-issued token ID. You can use this to call the [Get token information](https://developers.pismo.io/pismo-docs/reference/gettokeninfo) endpoint.
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `network_brand`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            * `vts` -  Visa
            * `mdes` - Mastercard
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `network_call_method`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            * `VTS_DEVICE_BINDING`
            * `TA`
            * `VTS_APPROVE_PROVSIONING`
            * `VTS_APPROVE_PROVISIONG_ISO`
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `card`
          </td>

          <td style={{ textAlign: "left" }}>
            object
          </td>

          <td style={{ textAlign: "left" }} />

          <td style={{ textAlign: "left" }} />
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `id`
          </td>

          <td style={{ textAlign: "left" }}>
            number
          </td>

          <td style={{ textAlign: "left" }}>
            Pismo-assigned card ID
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `type`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            Card type:

            * `PLASTIC`
            * `VIRTUAL`
            * `RECURRING`
            * `TEMPORARY`
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `program_id`
          </td>

          <td style={{ textAlign: "left" }}>
            number
          </td>

          <td style={{ textAlign: "left" }}>
            Program ID
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `bin`
          </td>

          <td style={{ textAlign: "left" }}>
            string
          </td>

          <td style={{ textAlign: "left" }}>
            Bank identification number
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `status`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            Card status:

            * `created`
            * `normal`
            * `damaged`
            * `warning`
            * `lost`
            * `unknown`
          </td>

          <td style={{ textAlign: "left" }}>
            No
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `stage`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            Card lifecycle status

            * `unknown`
            * `blocked`
            * `unblocked`
          </td>

          <td style={{ textAlign: "left" }}>
            No
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `combo_card`
          </td>

          <td style={{ textAlign: "left" }}>
            object
          </td>

          <td style={{ textAlign: "left" }} />

          <td style={{ textAlign: "left" }}>
            No
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `status`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            Card status:

            * `created`
            * `normal`
            * `damaged`
            * `warning`
            * `lost`
            * `unknown`
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            `original_network_data`
          </td>

          <td style={{ textAlign: "left" }}>
            object
          </td>

          <td style={{ textAlign: "left" }}>
            Refer to the [VISA Token Service (VTS)\
            Issuer API Specifications (JSON) manual](https://developer.visa.com/capabilities/token-service-provisioning) or the [Mastercard Customer Interface Specification manual](https://techdocs.mastercard.com/bundle/m_CI) for more information on the contents of this field. Note: The Mastercard manual requires a Mastercard Connect ID log in for access.
          </td>

          <td style={{ textAlign: "left" }}>
            No
          </td>
        </tr>
      </tbody>
    </Table>

    <br /><p style={{fontSize: "large", fontWeight: "bold"}}>Custom codes</p>

    <p>VTS = Visa, MDES = Mastercard.</p>

    | Custom code  | Description                                                       | VTS action code  | MDES action code |
    | :----------- | :---------------------------------------------------------------- | :--------------- | :--------------- |
    | `CCS`        | Card status =`CANCELLED`                                          | 46               | 05               |
    | `CED`        | Invalid expiration date. Exp date entered does not match Pismo's. | 54               | 05               |
    | `CNN`        | Card is not in`NORMAL` status                                     | 05               | 05               |
    | `EXPCRD`     | Expired card                                                      | 05               | 05               |
    | `FR2`        | Entered CVV2 is invalid                                           | N7               | 05               |
    | `FRB`        | `CREATED` status not allowed                                      | 05               | 05               |
    | `HSE`        | HSM failed to validate CVV2.                                      | 05               | 05               |
    | `NPL`        | Card not plastic. Issuer can override for virtual card.           | 05               | 05               |
    | `UBT`        | Blocked card. Legacy                                              | 05               | 05               |
    | `ELFR2`      | CVV2 retry limit exceeded                                         | 05               |  05              |
    | `MATPC`      |  Exceeded maximum active tokens per card                          | 05               |  05              |
    | `FRE`        |  Cryptogram data validation failed                                | 05               |  05              |
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample request</summary>

    ```json
    {
        "card":{
            "id": 134142,
            "type": "PLASTIC",
            "program_id": 1234,
            "bin": "5122"
        },
        "combo_card": { },
        "token_id": 432,
        "network_brand": "vts",
        "custom_codes": ["FRB"],
        "original_network_data": {

        }
    }
    ```
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}> Response fields</summary>

    <Table align={["left","left","left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Field
          </th>

          <th style={{ textAlign: "left" }}>
            Type
          </th>

          <th style={{ textAlign: "left" }}>
            Description
          </th>

          <th style={{ textAlign: "left" }}>
            Required
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            **`approve`**
          </td>

          <td style={{ textAlign: "left" }}>
            boolean
          </td>

          <td style={{ textAlign: "left" }}>
            Card approved flag
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            **`action_code`**
          </td>

          <td style={{ textAlign: "left" }}>
            string
          </td>

          <td style={{ textAlign: "left" }}>
            Decision code:

            * `00` - Approved
            * `05` - Not approved
            * `14` - Invalid PAN
            * `46` - Closed account
            * `54` - Invalid expiration date
            * `57` - Not permitted
            * `58` - Not allowed on terminal
            * `85` - Needs challenge
            * `96` - Issuer internal system error
            * `N7` - Invalid CVV2
          </td>

          <td style={{ textAlign: "left" }}>
            Yes
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            **`step_up_methods`**
          </td>

          <td style={{ textAlign: "left" }}>
            object array
          </td>

          <td style={{ textAlign: "left" }}>
            Needs challenge methods. At least one is required if used.
          </td>

          <td style={{ textAlign: "left" }}>
            Yes if `action_code` = `85`.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `method`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            One-time passcode (OTP) challenge method:

            * `OTPSMS` - SMS
            * `OTPAPP` - App
            * `OTPCALL` - Call
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `value`
          </td>

          <td style={{ textAlign: "left" }}>
            string
          </td>

          <td style={{ textAlign: "left" }}>
            Additional information for challenge - phone number, app, and so on.
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `platform`
          </td>

          <td style={{ textAlign: "left" }}>
            enum string
          </td>

          <td style={{ textAlign: "left" }}>
            Only used for Visa and only when the method is `OPTAPP`:

            * `IOS`
            * `ANDROID`
            * `WINDOWS`
            * `WEB`
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
             `source`
          </td>

          <td style={{ textAlign: "left" }}>
            string
          </td>

          <td style={{ textAlign: "left" }}>
            Only used for Visa and under certain conditions. This is the **Source Address** field as discussed in the VISA VTS manual and you should read that document for more information.
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>
      </tbody>
    </Table>
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample response </summary>

    ```json
    {
        "step_up_methods": [
            {
                "method": "OTPCALL",
                "value": "+551130039500"
            },
            {
                "method": "OTPSMS",
                "value": "5327"
            },
            {
                "method": "OTPAPP",
                "value": "app",
                "source": "com.issuer.banking://wallet",
                "platform": "ANDROID"
            }
        ],
        "approve": true,
        "action_code": "85"
    }
    ```
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Anti-fraud code sample (Go)</summary>

    ```Text Anti-fraud code sample
    package main

    // Anti-fraud code sample in Go

    //curl --location --request POST 'http://antifraudhost' \
    //--header 'x-pismo-sign: <your_signed_jwt>' \
    //--header 'Content-Type: application/json' \
    //--data-raw '{
    //    "card":{
    //        "id": 134142,
    //        "type": "PLASTIC"
    //    },
    //    "combo_card": null,
    //    "token_id": 432,
    //    "network_brand": "vts",
    //    "custom_codes": ["FRB", "BNB"],
    //    "original_network_data": {}
    //}'

    import (
    	"context"
    	"crypto/x509"
    	"encoding/json"
    	"encoding/pem"
    	"fmt"
    	"github.com/labstack/echo/v4"
    	"github.com/square/go-jose"
    	"io/ioutil"
    	"net/http"
    )

    type clientTokenDecision struct {
    	Approve       bool                 `json:"approve"`
    	ActionCode    string               `json:"action_code"`
    	StepUpMethods []clientStepUpMethod `json:"step_up_methods"`
    }

    type clientStepUpMethod struct {
    	Method   string `json:"method"`
    	Value    string `json:"value,omitempty"`
    	Source   string `json:"source"`
    	Platform string `json:"platform"`
    }

    func main() {
    	getPismoCertificates()
    	e := echo.New()
    	e.POST("/", handler)
    	e.Logger.Fatal(e.Start(":1323"))
    }

    var mapCertificates map[string]*x509.Certificate

    func getPismoCertificates() {
    	url := "https://sandbox.pismolabs.io/v1/certs"
    	httpReq, err := http.NewRequestWithContext(context.Background(), http.MethodGet, url, nil)
    	if err != nil {
    		panic(err)
    	}

    	client := http.Client{}
    	httpRes, err := client.Do(httpReq)
    	if err != nil {
    		panic(err)
    	}

    	if httpRes.StatusCode != http.StatusOK {
    		panic(err)
    	}

    	bRes, err := ioutil.ReadAll(httpRes.Body)
    	if err != nil {
    		panic(err)
    	}

    	tmpMap := make(map[string]string)
    	err = json.Unmarshal(bRes, &tmpMap)
    	if err != nil {
    		panic(err)
    	}

    	mapCertificates = make(map[string]*x509.Certificate)

    	for key, val := range tmpMap {
    		block, _ := pem.Decode([]byte(val))
    		if block == nil {
    			panic("cannot decode block")
    		}

    		cer, err := x509.ParseCertificate(block.Bytes)
    		if err != nil {
    			panic(err)
    		}
    		mapCertificates[key] = cer
    	}
    }

    func handler(c echo.Context) error {
    	tokenString := c.Request().Header.Get("X-Pismo-Sign")
    	valid := isTokenValid(tokenString)
    	if !valid {
    		return fmt.Errorf("certificate not valid")
    	}

    	k := clientTokenDecision{

    		Approve:    true,
    		ActionCode: "85",
    		StepUpMethods: []clientStepUpMethod{
    			{

    				Method: "OTPAPP",
    				Value:  "app.to.app",
    			},
    			{
    				Method: "OTPSMS",
    			},
    		},
    	}
    	return c.JSON(http.StatusOK, k)
    }

    func isTokenValid(tokenString string) bool {
    	jwsSignature, err := jose.ParseSigned(tokenString)
    	if err != nil {
    		return false

    	}

    	for _, sign := range jwsSignature.Signatures {
    		kid := sign.Header.KeyID
    		cert := mapCertificates[kid]
    		_, err := jwsSignature.Verify(cert.PublicKey)

    		if err != nil {
    			return false
    		}
    		break
    	}
    	return true
    }
    ```
  </details>
</details>

# Client anti-fraud webhook for banking transaction

This webhook is called during banking operations such as instant pay transactions. Specifically, it would be called during the processing for the following endpoints:

* [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer)
* [Pix reversal](https://developers.pismo.io/pismo-docs/reference/post-pix-reversal)
* [Pay bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay)
* [Perform cash-out](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-cashout) (integrated payments)
* [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments)
* [Create installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments)
* [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization)
* [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments)
* [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers)

<details>
  <summary style={{fontSize: "18px"}}><b>Webhook specifications</b></summary>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Request fields</summary>

    <HTMLBlock>
      {`
                                                                                                                                                                                                                                                                                                                                                  <table>
                                                                                                                                                                                                                                                                                                                                                  	<tr style="background-color: lightgrey;">
                                                                                                                                                                                                                                                                                                                                                  		<th>Field</th>;
                                                                                                                                                                                                                                                                                                                                                  		<th>Type</th>
                                                                                                                                                                                                                                                                                                                                                  		<th>Description</th>
                                                                                                                                                                                                                                                                                                                                                  		<th>Req</th>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>decision</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>string</td>
                                                                                                                                                                                                                                                                                                                                                      <td>Pismo decision<br>Enum: [ "<code>approve</code>". "<code>reject</code>" ]</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>id</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Request ID</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>datetime</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Call datetime in ISO 8601 format</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>account_id</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Pismo account ID</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>currency_code</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                      <td>string</td>
                                                                                                                                                                                                                                                                                                                                                  		<td> ISO 4217 currency code. For example: 986=Brazil, 840=US.</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>amount</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>number</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Transaction amount</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>origin</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Transaction origin:
                                                                                                                                                                                                                                                                                                                                                  			<br>Enum:[
                                                                                                                                                                                                                                                                                                                                                  					"<code>banking</code>", 
                                                                                                                                                                                                                                                                                                                                                            "<code>instant-pay</code>".
                                                                                                                                                                                                                                                                                                                                                            "<code>onus</code>"]
                                                                                                                                                                                                                                                                                                                                                  				</td>
                                                                                                                                                                                                                                                                                                                                                  				<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  			</tr>
                                                                                                                                                                                                                                                                                                                                                  			<tr>
                                                                                                                                                                                                                                                                                                                                                  				<td>
                                                                                                                                                                                                                                                                                                                                                  						<code>operation_type</code>
                                                                                                                                                                                                                                                                                                                                                  				</td>
                                                                                                                                                                                                                                                                                                                                                  				<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  				<td>Operation type:
                                                                                                                                                                                                                                                                                                                                                  					<br>Enum: [
                                                                                                                                                                                                                                                                                                                                                  						
                                                                                                                                                                                                                                                                                                                                                  							"<code>cashin</code>",
                                                                                                                                                                                                                                                                                                                                                                "<code>cashout</code>" ]
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td>
                                                                                                                                                                                                                                                                                                                                                  								<code>processing_code</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Processing code. For more information see 
                                                                                                                                                                                                                                                                                                                                                  							<a href="https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types">Processing codes and transaction types</a>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  						<td>
                                                                                                                                                                                                                                                                                                                                                  							
                                                                                                                                                                                                                                                                                                                                                  								<code>entities</code>
                                                                                                                                                                                                                                                                                                                                                  							
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Details of entities related to the transaction.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 30px;">
                                                                                                                                                                                                                                                                                                                                                  							
                                                                                                                                                                                                                                                                                                                                                  								<code>account</code>
                                                                                                                                                                                                                                                                                                                                                  							
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v1/cards/{cardId}/network-tokens/{tokenId}` | `gettokeninfo` | Get token information | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--token-lifecycle |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v1/pix/in/reversal` | `post-pix-reversal` | Pix reversal | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | Pay bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | Perform cash-out | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--transfer |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payments/v1/payments/installments` | `post-payments-v1-installments` | Create installments payment | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--installments-payments |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/payments` | `post-payments` | Create cash-in or cash-out | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /payment-methods/v2/transfers` | `post-transfers` | Create transfer | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-02 |

### Operation essentials

- **`GET /v1/cards/{cardId}/network-tokens/{tokenId}`** (`gettokeninfo`): security `BearerAuth`; required parameters `cardId` (path), `tokenId` (path); required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples `ERR93836`, `ERR9786`, `ERR5446`; events none listed.
- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /pix/v1/pix/in/reversal`** (`post-pix-reversal`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `end_to_end_id`, `reason`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0005`, `EPIX0020`, `PCE001`, `EPIX0045`, `EPIX0049`, `EPIX0084`, `EPIX0009`, `EPIX0010`, `EPIX0069`, `EPIX0132`, `EPIX0003`, `EPIX0041`, `EPIX0008`, `EPIX0071`, `EPIX0083`, `EPIX0085`, `EPIX0086`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0014`, `EPIX0043`, `EPIX0018`, `EPIX0030`; events `pix-financial-reconciliation-1`, `pix-pix-in-reversal-1`, `pix-pix-out-reversal-1`.
- **`POST /v1/bankslips/pay`** (`post-integrated-payments-api-v1-bankslips-pay`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`; response statuses 202, 400, 403, 404, 409, 500, 502, 504; error codes in examples `EIP0005`, `EIP0006`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0017`, `EIP0023`, `EIP0020`, `EIP0061`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0030`, `EIP0049`, `EIP0063`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0041`, `EIP0051`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `authorization-authorization-event-1`, `integrated-payments-bankslip-status-change-1`, `integrated-payments-financial-reconciliation-1`.
- **`POST /v1/transfers/cashout`** (`post-integrated-payments-api-v1-bankslips-cashout`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`, `processing_code`; response statuses 202, 400, 403, 409, 500, 502, 504; error codes in examples `EIP0003`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0016`, `EIP0017`, `EIP0020`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0029`, `EIP0030`, `EIP0031`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `integrated-payments-financial-reconciliation-1`, `integrated-payments-transaction-status-change-1`, `integrated-payments-transfer-out-created-1`.
- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /payments/v1/payments/installments`** (`post-payments-v1-installments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `account_id`, `charging_amount`, `processing_code`, `installments`; response statuses 201, 202, 400, 404, 409, 422, 500; error codes in examples `WP2P0000`, `WP2P0024`, `WP2P0025`, `WP2P0026`, `WP2P0027`, `WP2P0028`, `WP2P0029`, `WP2P0030`, `WP2P0005`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WLDG0006`, `WP2P0023`, `WP2P0022`, `WP2P0010`, `RULVAL0409`, `WP2P0000`, `WP2P0000`; events `authorization-authorization-event-1`.
- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/payments`** (`post-payments`): security `BearerAuth`; required parameters none declared; required body fields `account_id`, `amount`, `processing_code`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.
- **`POST /payment-methods/v2/transfers`** (`post-transfers`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `from`, `to`, `tracking_id`; response statuses 200, 201, 400, 401, 409, 422, 500; error codes in examples `WONP0001`, `WONB0001`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `platform-authorization-platform-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-integrated-payments-api-v1-bankslips-pay` | `authorization-authorization-event-1` |
| `post-payments-v1-installments` | `authorization-authorization-event-1` |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-bankslip-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transaction-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transfer-out-created-1` |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-pix-reversal` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-pix-reversal` | `pix-pix-in-reversal-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |
| `post-pix-reversal` | `pix-pix-out-reversal-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |
| `post-payments` | `platform-authorization-platform-authorization-1` |
| `post-transfers` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 1–837 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--transfer` — API reference: Banking - Integrated payments — Transfer
- `KU-API-card-issuing-tokenization--token-lifecycle` — API reference: Card issuing - Tokenization — Token lifecycle
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-CARD-card-tokenization-flow-and-events` — Card tokenization flow and events
- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-verifying-webhook-requests` — Verifying webhook requests
