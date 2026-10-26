---
ku_id: KU-API-card-issuing-disputes--supporting-forms
title: 'API reference: Card issuing - Disputes — Supporting forms'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Disputes.yaml
  sha256: 5c1d5513e1f3a4d1daa4d6bd654885c4edfeb5135eaa60b50f1a74d62031baad
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/operations_catalog.csv
  sha256: b218bf75940b0c374ca9e3a48fe92fb615b559e3192f263aff99b738b50a71cf
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/request_response_examples.csv
  sha256: ac921f2e8d0d154511b4550462e609cf6bebe3e6ce05dada157e0ed645a80856
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- post-v1-disputes-disputeId-forms
- put-v1-disputeform-forms
- post-v1-disputes-fraud-report
- put-v1-disputes-fraud-report
related_kus:
- KU-CARD-disputes-overview
- KU-CARD-visa-colloboration-questionaire-part-01
- KU-EVT-disputes-endpoint-generated-events
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — Supporting forms

**KU ID:** `KU-API-card-issuing-disputes--supporting-forms` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Supporting forms` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to handle supporting forms for specific dispute types

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/disputes/{disputeId}/forms` | `post-v1-disputes-disputeId-forms` | Create dispute form | no |
| `PUT /v1/disputes/{disputeId}/forms/{disputeFormId}` | `put-v1-disputeform-forms` | Update dispute form | no |
| `POST /v1/disputes/{disputeId}/fraud-report` | `post-v1-disputes-fraud-report` | Create dispute fraud report | no |
| `PUT /v1/disputes/{fraudReportId}/fraud-report` | `put-v1-disputes-fraud-report` | Update dispute fraud report | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes/{disputeId}/forms operationId=post-v1-disputes-disputeId-forms -->
### `POST /v1/disputes/{disputeId}/forms` — Create dispute form

- **operationId:** `post-v1-disputes-disputeId-forms`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Supporting forms`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a dispute form with more information to send to the network.
>
> You can create one of the following types of Expedited Billing Dispute Forms (EBDF):
>
> 1. **fraudDrfDocument** - Used for cases of fraud
>
> 2. **cardholderDisputeChargebackDrfDocument** -  Used when the cardholder disputes a purchase and notifies the card issuer.
>
> 3. **pointOfInteractionErrorsDrfDocument** -  Used when there's either a disagreement between parties or an error with the transaction. For example, a wrong value or a duplicate charge.
>
> For VISA, you need to fill out the `allocationQuestionnaire` (reason 11) or `collaborationQuestionnaire` (reason 12 and 13) form object. VISA's rules for filling out form fields can be found in [this guide document](https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire)
>
> For Elo, you need to fill out the `clearingElo` form object.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `DisputeFormRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_installment_id` | number | no | Dispute installment ID. If not passed, the first installment is used |  |
| `form` | object | yes | Field to register form used to send to network. |  |
| `form.ebdf` | object | no |  |  |
| `form.ebdf.fraudDrfDocument` | object (schema `FraudDrfDocumentStructure`) | no |  |  |
| `form.ebdf.cardholderDisputeChargebackDrfDocument` | object (schema `CardholderDisputeChargebackDrfDocumentStructure`) | no |  |  |
| `form.ebdf.pointOfInteractionErrorsDrfDocument` | object (schema `PointOfInteractionErrorsDrfDocumentStructure`) | no |  |  |
| `form.allocationQuestionnaire` | object (schema `VisaAllocationQuestionnaireDocumentStructure`) | no |  |  |
| `form.collaborationQuestionnaire` | object (schema `VisaCollaborationQuestionnaireDocumentStructure`) | no |  |  |
| `form.preArbitration` | object (schema `PreArbitration`) | no |  |  |
| `form.clearingElo` | object (schema `ClearingEloStructure`) | no |  |  |

Example `Create a Dispute Form Master with success`:

```json
{
  "dispute_installment_id": 0,
  "form": {
    "ebdf": {
      "fraudDrfDocument": {
        "numberOfItems": "1",
        "types": "CARD_CLOSED",
        "additionalInformation": "Test additional information",
        "chargebackRepresentative": "Test Representative",
        "cardIssuerRegion": "Europe",
        "cardholderVerificationMethod": {
          "onlinePIN": "1",
          "offlinePIN": "2",
          "signature": "3",
          "none": "4"
        }
      },
      "cardholderDisputeChargebackDrfDocument": {
        "transactionAmount": "100.00",
        "type": "PRODUCT_DISPUTE",
        "deliveryDateOfGoodsOrServices": "18-FEB-2018",
        "expectedDeliveryDateOfGoodOrServices": "18-FEB-2018",
        "returnDate": "18-FEB-2018",
        "cancellationDate": "18-FEB-2018",
        "cardholderParticipation": false,
        "disputeDetails": "Test Dispute details",
        "chargebackRepresentative": "Test Representative"
      },
      "pointOfInteractionErrorsDrfDocument": {
        "transactionAmount": "20000",
        "type": "DUPLICATE_DEBIT",
        "alternateMeansOfPaymentDetails": "Test alternate means of payment details",
        "disputeDetails": "Test Dispute details",
        "chargebackRepresentative": "Test Representative"
      }
    }
  }
}
```

Example `Create a Dispute Form Visa Allocation with success`:

```json
{
  "dispute_installment_id": 0,
  "form": {
    "allocationQuestionnaire": {
      "accountStatus": "AC"
    }
  }
}
```

Example `Create a Dispute Form Visa Collaboration with success`:

```json
{
  "dispute_installment_id": 0,
  "form": {
    "collaborationQuestionnaire": {
      "incorrectCurrencyReason": "CD",
      "authorizationRequestDeclinedValidDataInd": true,
      "explainWhyValidDataInclusionReason": "Explain why the inclusion of valid data would have caused the Authorization Request to be declined",
      "processingDateOver10DaysFmTransDateInd": true,
      "processingDateOver180DaysFmTransDateInd": true,
      "processingDateOver45DaysFmTransDateInd": true,
      "correctCurrency": 123,
      "cardholderDidNotAgreeDCC": "Y",
      "transactionCodeIncorrect": "CRI",
      "rolTransactionId": 123,
      "incorrectTransactionId": "string",
      "explainWhyCreditRefundProcessedInError": "Explain why the credit refund was processed in error",
      "issuerMasterFileAccountNumberInd": "Y",
      "receiptAccountNumberMatchInd": "Y",
      "matchingAuthTranId": 1234567890123456,
      "authorizationDate": "2022-05-20",
      "authorizationCode": "A12B34",
      "cardholderReceiptAmt": 12,
      "merchantDisputePriceDiffInd": "Y",
      "bothTransactionsOnSameAcctNumberInd": "Y",
      "duplicateTranId": "123456789012345",
      "duplicateTranDate": "2022-05-20",
      "duplicateTranAmount": 123,
      "duplicateARN": "112233445566778899001234",
      "issuerOrCardholderOtherAcctWithDiffVisaCardInd": "Y",
      "issuerEvidenceMerchantPassedOnFundsInd": "Y",
      "cardholderAttemptToResolve": "Y",
      "attemptToResolveProhLocalLaw": "Y",
      "otherTranSameMerchantInd": "Y",
      "providingPaymentProofOtherMeans": "A",
      "arn": "001122334455667788991234",
      "transactionID": "123456789012345",
      "merchantFacilitiesWithdrawn": false,
      "cardholderDeceased": false,
      "cancellationDate": "2022-05-20",
      "accountClosureDate": "2022-05-20",
      "cancellationMethod": "Cancellation Reason.",
      "disputeRelateToOffpremisesDistanceSellInd": "Y",
      "disputeRelateToInd": "Y",
      "contractDate": "2022-05-20",
      "merchandiseOrServices": "Merchandise",
      "serviceType": "T",
      "whatWasPurchased": "Provide details of what was purchased",
      "cardholderReceiveMerchandiseInd": "Y",
      "chReceivedOrExpectedMerchandise": "2022-05-20",
      "cardholderReturnMerchandiseInd": "Y",
      "cardholderReturnedMerchandiseDate": "2022-05-20",
      "returnedMerchandiseReceivedDate": "2022-05-20",
      "returnMethod": "FF",
      "howMerchandiseReturned": "Explain how the merchandise was returned",
      "shippingTrackingNumber": "Tracking Number",
      "cardholderAttemptReturnMerchandise": "Y",
      "attemptedReturnDate": "2022-05-20",
      "howChAttemptReturnAndDispOfMerchandise": "Provide a detailed description of how the cardholder attempted to return and the disposition of the merchandise",
      "merchantRefuseAdvise": "MRRM",
      "didCardholderCancel": "Y",
      "timeshareDate": "2022-05-20",
      "dateOfService": "2022-05-20",
      "certificationGuaranteedReservation": "GR",
      "cancellationPolicyProvidedInd": "Y",
      "whatWasOrdered": "What was ordered?",
      "whereIsMerchandiseLocated": "Where is the merchandise located?",
      "merchandiseWasCounterfeitDate": "2022-05-20",
      "descCounterfeitMerchandise": "Describe the counterfeit merchandise",
      "descDispOfCounterfeitMerchandise": "Describe the disposition of the counterfeit merchandise",
      "originalCreditNotAccepted": "R",
      "explain": "Explain",
      "creditVoucherTransactionReceipt": "Y",
      "creditVoucherTransactionReceiptDated": "Y",
      "creditVoucherOrTransactionReceiptDate": "2022-05-20",
      "cardholderCancelledReturnedMerchDate": "2022-05-20",
      "merchantInLiquidationOrReceivershipInd": "Y",
      "whatWasNotReceived": "What was not received?",
      "thirdPartyGiftCardInd": "Y",
      "visaComCardVirtualAccInd": "Y",
      "virtualAccFinancialLossInd": "Y",
      "didMerchantCancelInd": "Y",
      "merchantCancellationDate": "2022-05-20",
      "nonReceiptOfTravelServicesInd": "Y",
      "disputeInvolveBondingAuthorityInd": "Y",
      "explainAttemptToResolveWithBondAuth": "Provide an explanation of the attempt to resolve the dispute with the bonding authority/insurance scheme or where the information was obtained to confirm an insufficient bond/insurance scheme",
      "bondAuthLetterOrAdviceDate": "2022-05-20",
      "purchasedInfo": "Provide detailed description of what was purchased and an explanation of the dispute",
      "expectedReceiptDate": "2022-05-20",
      "expectedReceiptTime": "10:30",
      "explainDisputePriorDeliveryDate": "Explanation of dispute initiated prior to the expected delivery date",
      "didCardholderCancelPriorExpectedDate": "Y",
      "merchandiseDeliveredWrongLocation": "Y",
      "lateDeliveryWrongLocation": "Provide address of the agreed location or details of late delivery",
      "damagedOrDefectiveOrderInfo": "What was ordered and how it was damaged or defective?",
      "merchandiseReceivedDate": "2022-05-20",
      "cardholderMerchantPreviousNegotiationEvidence": "Y",
      "whenNegotiationsBegin": "2022-05-20",
      "explainPrevNegotiation": "Explain the previous ongoing negotiations between the cardholder and merchant.",
      "cardholderFirstNotifiedIssuerDisputeDate": "2022-05-20",
      "merchantReceivedReturnedMerchandiseDate": "2022-05-20",
      "serviceReceivedDate": "2022-05-20",
      "howMerchandiseOrServiceMisrepresented": "How was the merchandise or service misrepresented?",
      "merchandiseServiceReceivedDate": "2022-05-20",
      "orderDetailsNotAsDescribed": "Provide details of what was ordered and not as described",
      "merchantAcceptCancellationInd": "Y",
      "purchasedInfoAndQualityIssue": "Provide information about what was purchased and the quality issue",
      "didCardholderPayWorkRedone": "Y",
      "howTermsOfContractNotHonoredByMerchant": "Provide details how the terms of the contract were either not honored by the merchant or not as described",
      "nonFiatCurrencyNotDelivered": "Y",
      "merchandiseDeliveredLate": "Y",
      "merchantInBankruptcyLiquidationInd": "Y",
      "nonFiatCurrencyNotMatching": "Y",
      "dispositionOfMerchandise": "a",
      "merchantAcceptInd": "Y",
      "explainCreditIssuedLateDetailsOfNegotiations": "Pending"
    }
  }
}
```

Example `Create a Dispute Form Clearing Elo with success`:

```json
{
  "dispute_installment_id": 0,
  "form": {
    "clearingElo": {
      "transactionDestinationInstitutionIdCode": "",
      "filePathMessageNumber": "",
      "additionalDataRecord": {
        "airportTaxValue": "000000000000",
        "changeValue": "00000000000",
        "codeProduct": "071",
        "conditionalCodeChipTransaction": "1",
        "cpfOrCnpj": "00000000000000",
        "feePaymentInput": "00000",
        "indicatorMovement": "0",
        "installmentNumber": "000",
        "logicalNumberEquipment": "20172289",
        "numberInstallmentsTransaction": "000",
        "pointOfSale": "000000000000001",
        "referenceNumberDispute": "000000",
        "transactionCode": "06",
        "transactionIndicator": "8",
        "transactionSubCode": "01",
        "transactionValue": "000000000000",
        "walletId": "00000000000",
        "authorizationCode": "661810",
        "caller": "ELO",
        "clearingType": "CREDIT",
        "correlationId": "a40465a2-82af-4721-8938-383xxxxxxxxx",
        "endpoint": "000666",
        "headerServiceFile": {
          "codeAcquirer": "0000",
          "codeProcessor": "3178",
          "emittingBank": "0985",
          "fileVersion": "231",
          "flagCode": "007",
          "futureUse2": "0",
          "returnDateArchive": "00000000",
          "returnTimeArchive": "000000",
          "routeIndicatorArchive": "1",
          "sendDate": "20230717",
          "serviceCode": "10",
          "shipmentNumber": "0177",
          "shippingDate": "20230717",
          "shippingTimeArchive": "152300",
          "transactionSubCode": "B0",
          "windowNumber": null
        },
        "mainDataRecord": {
          "authorizationOrCancellationOriginIndicator": "1",
          "cardholderVerificationMethod": "1",
          "cardNumber": "",
          "codeAcquirer": "9000",
          "codeAuthorizationTransaction": "661810",
          "codeCurrency": "986",
          "codeFlag": "007",
          "codeReasonDispute": "00",
          "futureUse2": "00",
          "futureUse4": "0",
          "futureUse5": "0000",
          "identificationTransaction": "1",
          "numberReferenceTransaction": "70090003198000000723318",
          "pointOfSaleCity": "ZAMBAS",
          "pointOfSaleCountryCode": "BR",
          "pointOfSaleMcc": "6531",
          "pointOfSaleName": "Lns",
          "posEntryMode": "82",
          "processCode": "53",
          "processingDate": "20230717",
          "sellValue": "000000001000",
          "terminalCapability": "V",
          "transactionCode": "06",
          "transactionDate": "20230717",
          "transactionSubCode": "00",
          "transactionTime": "092225"
        },
        "messageNumber": "157",
        "orgId": "TN-41234404-7994-46d5-83d6-a55cxxxxxxxx",
        "registrationFundsTransferData": {
          "cardBIN": "00000000",
          "identificationNumberOfPersonImpacted": "18230565371336",
          "last4DigitsCard": "0000",
          "nameCarrier": "bR1YsI xhDVQNL",
          "originFunds": "02",
          "phoneCarrier": "00000000000",
          "transactionCode": "06",
          "transactionSubCode": "P2P",
          "typePayment": "06"
        },
        "registrationPaymentServiceData": {
          "amountAuthorized": "000000001000",
          "codeAnswerAuthorization": "00",
          "codeCurrencyValueAuthorized": "986",
          "futureUse19": "00",
          "identifierTransaction": "202289723318",
          "indicatorBusinessElectronic": "00",
          "transactionCode": "06",
          "transactionSubCode": "05",
          "valueAuthorized": "000000001000"
        },
        "s3Path": "",
        "settlementCountryDataRecord": {
          "countryCodeSettlement": "BR",
          "dateLiquidationTransaction": "20230718",
          "dateMovementTransactionOriginal": "00000000",
          "municipalCode": "0000000",
          "networkReferenceId": "1982391A0020319",
          "pointOfSaleMarketplaceCode": "000000000000000",
          "quantityDaysFinancialTransaction": "001",
          "transactionCode": "06",
          "transactionSubCode": "02",
          "valueExchange": "0000000000",
          "zipCodeEstablishmentCommercial": "i7qQFhLh"
        }
      }
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFormResponse`) |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute form ID. | example: 122 |
| `dispute_installment_id` | number | no | If necessary to join Form to Installment. If not passed, first installment is used. | nullable: true |
| `status` | string (schema `DisputeFormStatus`) | no | Dispute form status. | enum: ["PENDING", "PROCESSED", "FAILED", "INACTIVE"]; example: "PENDING" |
| `network` | string | no | Network for dispute Form. | enum: ["PRIMITIVE_ON_US", "PRIMITIVE"]; example: "PRIMITIVE" |
| `form` | object | no |  |  |
| `form.ebdf` | object | no |  |  |
| `form.ebdf.fraudDrfDocument` | object (schema `FraudDrfDocumentStructure`) | no |  |  |
| `form.ebdf.cardholderDisputeChargebackDrfDocument` | object (schema `CardholderDisputeChargebackDrfDocumentStructure`) | no |  |  |
| `form.ebdf.pointOfInteractionErrorsDrfDocument` | object (schema `PointOfInteractionErrorsDrfDocumentStructure`) | no |  |  |
| `form.allocationQuestionnaire` | object (schema `VisaAllocationQuestionnaireDocumentStructure`) | no |  |  |
| `form.collaborationQuestionnaire` | object (schema `VisaCollaborationQuestionnaireDocumentStructure`) | no |  |  |
| `form.preArbitration` | object (schema `PreArbitration`) | no |  |  |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `update_at` | string | no | Update date, format = yyyy-mm-dd | format: "date"; example: "2021-02-22" |
| `update_at_utc` | string | no | Update UTC date | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `dispute_form_type` | object (schema `DisputeFormType`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`, `KU-CARD-visa-colloboration-questionaire-part-01`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=PUT path=/v1/disputes/{disputeId}/forms/{disputeFormId} operationId=put-v1-disputeform-forms -->
### `PUT /v1/disputes/{disputeId}/forms/{disputeFormId}` — Update dispute form

- **operationId:** `put-v1-disputeform-forms`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Supporting forms`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a dispute form - only if status is `PENDING` or `FAILED`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |
| `disputeFormId` | path | yes | number | Dispute form ID |  |

#### Request body

Required: no

> NOTE: When chargebackEbdfDocuments is used for automatic EBDF document generation for fraudDrfDocument (or) cardholderDisputeChargebackDrfDocument (or) pointOfInteractionErrorsDrfDocument.

**Content type `application/json`** — schema: object (schema `DisputeFormRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_installment_id` | number | no | Dispute installment ID. If not passed, the first installment is used |  |
| `form` | object | yes | Field to register form used to send to network. |  |
| `form.ebdf` | object | no |  |  |
| `form.ebdf.fraudDrfDocument` | object (schema `FraudDrfDocumentStructure`) | no |  |  |
| `form.ebdf.cardholderDisputeChargebackDrfDocument` | object (schema `CardholderDisputeChargebackDrfDocumentStructure`) | no |  |  |
| `form.ebdf.pointOfInteractionErrorsDrfDocument` | object (schema `PointOfInteractionErrorsDrfDocumentStructure`) | no |  |  |
| `form.allocationQuestionnaire` | object (schema `VisaAllocationQuestionnaireDocumentStructure`) | no |  |  |
| `form.collaborationQuestionnaire` | object (schema `VisaCollaborationQuestionnaireDocumentStructure`) | no |  |  |
| `form.preArbitration` | object (schema `PreArbitration`) | no |  |  |
| `form.clearingElo` | object (schema `ClearingEloStructure`) | no |  |  |

Example `Update a Dispute Form Master with success`:

```json
{
  "dispute_installment_id": 0,
  "form": {
    "ebdf": {
      "fraudDrfDocument": {
        "numberOfItems": "1",
        "types": "CARD_CLOSED",
        "additionalInformation": "Test additional information",
        "chargebackRepresentative": "Test Representative",
        "cardIssuerRegion": "Europe",
        "cardholderVerificationMethod": {
          "onlinePIN": "1",
          "offlinePIN": "2",
          "signature": "3",
          "none": "4"
        }
      },
      "cardholderDisputeChargebackDrfDocument": {
        "transactionAmount": "100.00",
        "type": "PRODUCT_DISPUTE",
        "deliveryDateOfGoodsOrServices": "18-FEB-2018",
        "expectedDeliveryDateOfGoodOrServices": "18-FEB-2018",
        "returnDate": "18-FEB-2018",
        "cancellationDate": "18-FEB-2018",
        "cardholderParticipation": false,
        "disputeDetails": "Test Dispute details",
        "chargebackRepresentative": "Test Representative"
      },
      "pointOfInteractionErrorsDrfDocument": {
        "transactionAmount": "20000",
        "type": "DUPLICATE_DEBIT",
        "alternateMeansOfPaymentDetails": "Test alternate means of payment details",
        "disputeDetails": "Test Dispute details",
        "chargebackRepresentative": "Test Representative"
      }
    }
  }
}
```

Example `Update a Dispute Form Visa with success`:

```json
{
  "dispute_installment_id": 0,
  "form": {
    "collaborationQuestionnaire": {
      "incorrectCurrencyReason": "CD",
      "authorizationRequestDeclinedValidDataInd": true,
      "explainWhyValidDataInclusionReason": "Explain why the inclusion of valid data would have caused the Authorization Request to be declined",
      "processingDateOver10DaysFmTransDateInd": true,
      "processingDateOver180DaysFmTransDateInd": true,
      "processingDateOver45DaysFmTransDateInd": true,
      "correctCurrency": 123,
      "cardholderDidNotAgreeDCC": "Y",
      "transactionCodeIncorrect": "CRI",
      "rolTransactionId": 123,
      "incorrectTransactionId": "string",
      "explainWhyCreditRefundProcessedInError": "Explain why the credit refund was processed in error",
      "issuerMasterFileAccountNumberInd": "Y",
      "receiptAccountNumberMatchInd": "Y",
      "matchingAuthTranId": 1234567890123456,
      "authorizationDate": "2022-05-20",
      "authorizationCode": "A12B34",
      "cardholderReceiptAmt": 12,
      "merchantDisputePriceDiffInd": "Y",
      "bothTransactionsOnSameAcctNumberInd": "Y",
      "duplicateTranId": "123456789012345",
      "duplicateTranDate": "2022-05-20",
      "duplicateTranAmount": 123,
      "duplicateARN": "112233445566778899001234",
      "issuerOrCardholderOtherAcctWithDiffVisaCardInd": "Y",
      "issuerEvidenceMerchantPassedOnFundsInd": "Y",
      "cardholderAttemptToResolve": "Y",
      "attemptToResolveProhLocalLaw": "Y",
      "otherTranSameMerchantInd": "Y",
      "providingPaymentProofOtherMeans": "A",
      "arn": "001122334455667788991234",
      "transactionID": "123456789012345",
      "merchantFacilitiesWithdrawn": false,
      "cardholderDeceased": false,
      "cancellationDate": "2022-05-20",
      "accountClosureDate": "2022-05-20",
      "cancellationMethod": "Cancellation Reason.",
      "disputeRelateToOffpremisesDistanceSellInd": "Y",
      "disputeRelateToInd": "Y",
      "contractDate": "2022-05-20",
      "merchandiseOrServices": "Merchandise",
      "serviceType": "T",
      "whatWasPurchased": "Provide details of what was purchased",
      "cardholderReceiveMerchandiseInd": "Y",
      "chReceivedOrExpectedMerchandise": "2022-05-20",
      "cardholderReturnMerchandiseInd": "Y",
      "cardholderReturnedMerchandiseDate": "2022-05-20",
      "returnedMerchandiseReceivedDate": "2022-05-20",
      "returnMethod": "FF",
      "howMerchandiseReturned": "Explain how the merchandise was returned",
      "shippingTrackingNumber": "Tracking Number",
      "cardholderAttemptReturnMerchandise": "Y",
      "attemptedReturnDate": "2022-05-20",
      "howChAttemptReturnAndDispOfMerchandise": "Provide a detailed description of how the cardholder attempted to return and the disposition of the merchandise",
      "merchantRefuseAdvise": "MRRM",
      "didCardholderCancel": "Y",
      "timeshareDate": "2022-05-20",
      "dateOfService": "2022-05-20",
      "certificationGuaranteedReservation": "GR",
      "cancellationPolicyProvidedInd": "Y",
      "whatWasOrdered": "What was ordered?",
      "whereIsMerchandiseLocated": "Where is the merchandise located?",
      "merchandiseWasCounterfeitDate": "2022-05-20",
      "descCounterfeitMerchandise": "Describe the counterfeit merchandise",
      "descDispOfCounterfeitMerchandise": "Describe the disposition of the counterfeit merchandise",
      "originalCreditNotAccepted": "R",
      "explain": "Explain",
      "creditVoucherTransactionReceipt": "Y",
      "creditVoucherTransactionReceiptDated": "Y",
      "creditVoucherOrTransactionReceiptDate": "2022-05-20",
      "cardholderCancelledReturnedMerchDate": "2022-05-20",
      "merchantInLiquidationOrReceivershipInd": "Y",
      "whatWasNotReceived": "What was not received?",
      "thirdPartyGiftCardInd": "Y",
      "visaComCardVirtualAccInd": "Y",
      "virtualAccFinancialLossInd": "Y",
      "didMerchantCancelInd": "Y",
      "merchantCancellationDate": "2022-05-20",
      "nonReceiptOfTravelServicesInd": "Y",
      "disputeInvolveBondingAuthorityInd": "Y",
      "explainAttemptToResolveWithBondAuth": "Provide an explanation of the attempt to resolve the dispute with the bonding authority/insurance scheme or where the information was obtained to confirm an insufficient bond/insurance scheme",
      "bondAuthLetterOrAdviceDate": "2022-05-20",
      "purchasedInfo": "Provide detailed description of what was purchased and an explanation of the dispute",
      "expectedReceiptDate": "2022-05-20",
      "expectedReceiptTime": "10:30",
      "explainDisputePriorDeliveryDate": "Explanation of dispute initiated prior to the expected delivery date",
      "didCardholderCancelPriorExpectedDate": "Y",
      "merchandiseDeliveredWrongLocation": "Y",
      "lateDeliveryWrongLocation": "Provide address of the agreed location or details of late delivery",
      "damagedOrDefectiveOrderInfo": "What was ordered and how it was damaged or defective?",
      "merchandiseReceivedDate": "2022-05-20",
      "cardholderMerchantPreviousNegotiationEvidence": "Y",
      "whenNegotiationsBegin": "2022-05-20",
      "explainPrevNegotiation": "Explain the previous ongoing negotiations between the cardholder and merchant.",
      "cardholderFirstNotifiedIssuerDisputeDate": "2022-05-20",
      "merchantReceivedReturnedMerchandiseDate": "2022-05-20",
      "serviceReceivedDate": "2022-05-20",
      "howMerchandiseOrServiceMisrepresented": "How was the merchandise or service misrepresented?",
      "merchandiseServiceReceivedDate": "2022-05-20",
      "orderDetailsNotAsDescribed": "Provide details of what was ordered and not as described",
      "merchantAcceptCancellationInd": "Y",
      "purchasedInfoAndQualityIssue": "Provide information about what was purchased and the quality issue",
      "didCardholderPayWorkRedone": "Y",
      "howTermsOfContractNotHonoredByMerchant": "Provide details how the terms of the contract were either not honored by the merchant or not as described",
      "nonFiatCurrencyNotDelivered": "Y",
      "merchandiseDeliveredLate": "Y",
      "merchantInBankruptcyLiquidationInd": "Y",
      "nonFiatCurrencyNotMatching": "Y",
      "dispositionOfMerchandise": "a",
      "merchantAcceptInd": "Y",
      "explainCreditIssuedLateDetailsOfNegotiations": "Pending"
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFormResponse`) |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute form ID. | example: 122 |
| `dispute_installment_id` | number | no | If necessary to join Form to Installment. If not passed, first installment is used. | nullable: true |
| `status` | string (schema `DisputeFormStatus`) | no | Dispute form status. | enum: ["PENDING", "PROCESSED", "FAILED", "INACTIVE"]; example: "PENDING" |
| `network` | string | no | Network for dispute Form. | enum: ["PRIMITIVE_ON_US", "PRIMITIVE"]; example: "PRIMITIVE" |
| `form` | object | no |  |  |
| `form.ebdf` | object | no |  |  |
| `form.ebdf.fraudDrfDocument` | object (schema `FraudDrfDocumentStructure`) | no |  |  |
| `form.ebdf.cardholderDisputeChargebackDrfDocument` | object (schema `CardholderDisputeChargebackDrfDocumentStructure`) | no |  |  |
| `form.ebdf.pointOfInteractionErrorsDrfDocument` | object (schema `PointOfInteractionErrorsDrfDocumentStructure`) | no |  |  |
| `form.allocationQuestionnaire` | object (schema `VisaAllocationQuestionnaireDocumentStructure`) | no |  |  |
| `form.collaborationQuestionnaire` | object (schema `VisaCollaborationQuestionnaireDocumentStructure`) | no |  |  |
| `form.preArbitration` | object (schema `PreArbitration`) | no |  |  |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `update_at` | string | no | Update date, format = yyyy-mm-dd | format: "date"; example: "2021-02-22" |
| `update_at_utc` | string | no | Update UTC date | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `dispute_form_type` | object (schema `DisputeFormType`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes/{disputeId}/fraud-report operationId=post-v1-disputes-fraud-report -->
### `POST /v1/disputes/{disputeId}/fraud-report` — Create dispute fraud report

- **operationId:** `post-v1-disputes-fraud-report`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Supporting forms`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a dispute fraud report and one related installment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `DisputeFraudReportRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_installment_id` | number | no | Related dispute installment ID. If not passed, first Installment is used. | example: 1 |
| `report` | object (schema `DisputeFraudReportDocumentStructure`) | yes |  |  |

Example `Create a Dispute Fraud Report with success`:

```json
{
  "dispute_installment_id": 1,
  "report": {
    "acct_status": "ACCT_IS_OPEN",
    "chgbk_indicator": "1",
    "cvc_invalid_indicator": "Y",
    "device_type": "1",
    "fraud_type": "00",
    "report_date": "2021-02-11",
    "sub_type": "K"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFraudReportResponse`) |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_report_id` | number | no | Dispute fraud report ID. | example: 1 |
| `dispute_id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `dispute_installment_id` | number | no | Dispute installment related to dispute fraud report. | example: 1 |

200 Example `Created with success`:

```json
{
  "fraud_report_id": 1,
  "dispute_id": 1,
  "dispute_installment_id": 1
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`, `KU-EVT-disputes-endpoint-generated-events`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=PUT path=/v1/disputes/{fraudReportId}/fraud-report operationId=put-v1-disputes-fraud-report -->
### `PUT /v1/disputes/{fraudReportId}/fraud-report` — Update dispute fraud report

- **operationId:** `put-v1-disputes-fraud-report`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Supporting forms`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a fraud report.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `fraudReportId` | path | yes | number | Dispute fraud report ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `DisputeFraudReportUpdate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `report` | object (schema `DisputeFraudReportDocumentStructure`) | yes |  |  |

Example `Update a Dispute Fraud Report with success`:

```json
{
  "report": {
    "acct_status": "ACCT_IS_OPEN",
    "chgbk_indicator": "1",
    "cvc_invalid_indicator": "Y",
    "device_type": "1",
    "fraud_type": "01",
    "report_date": "2021-02-11",
    "sub_type": "K"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFraudReportResponse`) |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_report_id` | number | no | Dispute fraud report ID. | example: 1 |
| `dispute_id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `dispute_installment_id` | number | no | Dispute installment related to dispute fraud report. | example: 1 |

200 Example `Updated with success`:

```json
{
  "fraud_report_id": 1,
  "dispute_id": 1,
  "dispute_installment_id": 1
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/FraudDrfDocumentStructure -->
### Schema `FraudDrfDocumentStructure`

Pointer: `#/components/schemas/FraudDrfDocumentStructure`. Type: object (schema `FraudDrfDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `numberOfItems` | string | no | Number of transactions being disputed as string. | maxLength: 19; example: "1" |
| `types` | string | no | Enter any of the valid values comma separated.<br><br>Valid Values/Format: `CARD_CLOSED`, `REPORT_SAFE`, `CAPTURE_CARD`, `LOST_STOLEN`, `COUNTERFEIT`, `RC_4837`, `RC_4840`<br><br>`RC_4837` = Reason code 4837 (Mastercard - fraud)<br><br>`RC_4840` = Reason code 4840 (Mastercard - fraudelent processing of transaction) | enum: ["CARD_CLOSED", "REPORT_SAFE", "CAPTURE_CARD", "LOST_STOLEN", "COUNTERFEIT", "RC_4837", "RC_4840"]; example: "CARD_CLOSED" |
| `additionalInformation` | string | no | Additional information, if needed, 1000 chars max.<br><br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 1000; example: "Test additional information" |
| `chargebackRepresentative` | string | no | Customer Service/Chargeback Representative<br><br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 25; example: "Test representative" |
| `cardIssuerRegion` | string | no | Card issuer region.<br><br>Valid Values:<br><br>   `AP` - Asian Pacific<br><br>   `Europe` - Europe<br><br>   `NAM` - North America<br><br>   `LAC` - Latin America and Caribbean<br><br>   `MEA` - Middle East and Africa | enum: ["AP", "Europe", "NAM", "LAC", "MEA"]; example: "Europe" |
| `cardholderVerificationMethod` | object (schema `CardholderVerificationMethodStructure`) | no |  |  |

<!-- schema: #/components/schemas/CardholderDisputeChargebackDrfDocumentStructure -->
### Schema `CardholderDisputeChargebackDrfDocumentStructure`

Pointer: `#/components/schemas/CardholderDisputeChargebackDrfDocumentStructure`. Type: object (schema `CardholderDisputeChargebackDrfDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transactionAmount` | string | no | Transaction amount.<br><br> Length: 0-12<br><br> Valid Values/Format: Numeric | example: "100.00" |
| `type` | string | no | Cardholder dispute type. | enum: ["PRODUCT_DISPUTE", "NOT_PROVIDED", "DIGITAL_GOODS", "CREDIT_NOT_PROCESSED", "COUNTERFEIT", "RECURRING_CANCELLED", "RECURRING_DISCLOSURE", "ADDENDUM_DISPUTE", "HOTEL_NO_SHOW", "PURCHASE_INCOMPLETE", "CANCELLATION_AGREEMENT", "POSTED_CREDIT", "FAILED_TRAVEL"]; minLength: 11; maxLength: 22; example: "PRODUCT_DISPUTE" |
| `deliveryDateOfGoodsOrServices` | string | no | In case of `PRODUCT_DISPUTE`, goods or services delivery date. Format = dd-MMM-yyyy<br> | maxLength: 11; example: "18-FEB-2018" |
| `expectedDeliveryDateOfGoodOrServices` | string | no | In case of `NOT_PROVIDED`, goods or services expected delivery date. Format = dd-MMM-yyyy | maxLength: 11; example: "18-FEB-2018" |
| `returnDate` | string | no | In case of `DIGITAL_GOODS`, return or cancellation of the goods or services. Format = dd-MMM-yyyy | maxLength: 11; example: "18-FEB-2018" |
| `cancellationDate` | string | no | In case of `RECURRING_CANCELLED`, cancellation of the goods or services. Format = dd-MMM-yyyy | maxLength: 11; example: "18-FEB-2018" |
| `cardholderParticipation` | boolean | no | Did the cardholder participate in the transaction? | example: false |
| `disputeDetails` | string | no | Describe the cardholder’s complaint in sufficient detail to meet the requirements for the chargeback as described in the Chargeback Guide and to enable all parties to understand the dispute.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=)<br> | maxLength: 3000; example: "Test dispute details..." |
| `chargebackRepresentative` | string | no | Customer service/chargeback representative.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=)<br> | maxLength: 25; example: "Ahsta LaVista Baybee" |

<!-- schema: #/components/schemas/PointOfInteractionErrorsDrfDocumentStructure -->
### Schema `PointOfInteractionErrorsDrfDocumentStructure`

Pointer: `#/components/schemas/PointOfInteractionErrorsDrfDocumentStructure`. Type: object (schema `PointOfInteractionErrorsDrfDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transactionAmount` | string | no | The transaction amount as string. | maxLength: 12; example: "20000" |
| `type` | string | no | Error type enum, i.e. `DUPLICATE_DEBIT` | enum: ["DUPLICATE_DEBIT", "INCORRECT_AMOUNT", "LTD_TRANSACTION", "CURRENCY_DISPUTE", "UNREASONABLE_AMOUNT", "DUPLICATE_TRANSACTION", "MERCHANT_CREDIT", "IMPROPER_MERCHANT_SURCHARGE"]; example: "DUPLICATE_DEBIT" |
| `alternateMeansOfPaymentDetails` | string | no | In case of `DUPLICATE_DEBIT`, Alternate means of payment details. Max length = 55 chars.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=)<br> | maxLength: 55; example: "Test alternate means of payment details" |
| `disputeDetails` | string | no | Describe the cardholder's complaint in sufficient detail to meet the requirements for the chargeback as described in the Chargeback Guide and to enable all parties to understand the dispute.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 4800; example: "Test Dispute details" |
| `chargebackRepresentative` | string | no | Customer service/chargeback representative.<br><br> Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 25; example: "Test Representative" |

<!-- schema: #/components/schemas/VisaAllocationQuestionnaireDocumentStructure -->
### Schema `VisaAllocationQuestionnaireDocumentStructure`

Pointer: `#/components/schemas/VisaAllocationQuestionnaireDocumentStructure`. Type: object (schema `VisaAllocationQuestionnaireDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accountStatus` | string | yes | Valid in VISA Authorization Flux (reason code 11).<br><br>  `AC` = Account closed<br><br>  `CP` = Credit problem<br><br>  `F` = Fraud<br><br> | enum: ["AC", "CP", "F"]; example: "AC" |
| `oneAuthForMultipleSalesInd` | string | no | Valid in VISA Authorization Flux (reason code 11). | enum: ["Y", "N"]; example: "Y" |

<!-- schema: #/components/schemas/VisaCollaborationQuestionnaireDocumentStructure -->
### Schema `VisaCollaborationQuestionnaireDocumentStructure`

Pointer: `#/components/schemas/VisaCollaborationQuestionnaireDocumentStructure`. Type: object (schema `VisaCollaborationQuestionnaireDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `incorrectCurrencyReason` | string | no | Valid in VISA Processing Errors Flux (reason code 12.3). | enum: ["CD", "DD"]; example: "CD" |
| `authorizationRequestDeclinedValidDataInd` | boolean | no | Valid in VISA Processing Errors Flux (reason code 12). | example: true |
| `explainWhyValidDataInclusionReason` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 10000; example: "Explain why the inclusion of valid data would have caused the Authorization Request to be declined" |
| `correctCurrency` | integer | no | Valid in VISA Processing Errors Flux (reason code 12). | example: 986 |
| `cardholderDidNotAgreeDCC` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `transactionCodeIncorrect` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["CRI", "CRD", "DCR"]; example: "CRI" |
| `rolTransactionId` | number | no | Valid in VISA Processing Errors Flux (reason code 12). | example: 123 |
| `incorrectTransactionId` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 17 |
| `explainWhyCreditRefundProcessedInError` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 10000; example: "Explain why the credit refund was processed in error" |
| `issuerMasterFileAccountNumberInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `receiptAccountNumberMatchInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `cardholderReceiptAmt` | number | no | Valid in VISA Processing Errors Flux (reason code 12). | example: 12 |
| `merchantDisputePriceDiffInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `bothTransactionsOnSameAcctNumberInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `duplicateTranId` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | example: "123456789012345" |
| `issuerOrCardholderOtherAcctWithDiffVisaCardInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `issuerEvidenceMerchantPassedOnFundsInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `cardholderAttemptToResolve` | string | no | Valid in VISA Processing Errors Flux (reason code 12 and 13). | enum: ["Y", "N"]; example: "Y" |
| `attemptToResolveProhLocalLaw` | string | no | Valid in VISA Processing Errors Flux (reason code 12 and 13). | enum: ["Y", "N"]; example: "Y" |
| `otherTranSameMerchantInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `providingPaymentProofOtherMeans` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["A", "T", "C", "F", "V", "S", "O"]; example: "A" |
| `arn` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 24; example: "001122334455667788991234" |
| `transactionID` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 15; example: "123456789012345" |
| `merchantFacilitiesWithdrawn` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: false |
| `cardholderDeceased` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: false |
| `cancellationDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `contactMethodWithMerchantInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantEmailInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantCallCenterInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantMailInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantSMSInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantInPersonInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantWebformInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMerchantDetailsPhoneNumber` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `contactMerchantDetailsEmailAddress` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `contactMerchantDetailsPhysicalAddress` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `contactMerchantDetailsApplicationName` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `otherFormOfPaymentInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `otherFormOfPaymentDesc` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `accountClosureDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cancellationMethod` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000 |
| `disputeRelateToOffpremisesDistanceSellInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"] |
| `disputeRelateToInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `contractDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `merchandiseOrServices` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Merchandise", "Services"]; example: "Merchandise" |
| `serviceType` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["T", "G", "O"]; example: "T" |
| `whatWasPurchased` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide details of what was purchased..." |
| `cardholderReceiveMerchandiseInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `chReceivedOrExpectedMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cardholderReturnMerchandiseInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `cardholderReturnedMerchandiseDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `returnedMerchandiseReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `returnMethod` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["FF", "FE", "D", "U", "P", "O"]; example: "FF" |
| `howMerchandiseReturned` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explain how the merchandise was returned..." |
| `shippingTrackingNumber` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 50; example: "774-4u7u3-u4u4u-35347" |
| `cardholderAttemptReturnMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"] |
| `attemptedReturnDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "2022-05-20" |
| `howChAttemptReturnAndDispOfMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide a detailed description of how the cardholder attempted to return and the disposition of the merchandise." |
| `merchantRefuseAdvise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["MRRM", "MICNRM"]; example: "MRRM" |
| `didCardholderCancel` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `didCardholderCancelBeforeShipping` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `timeshareDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `dateOfService` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `certificationGuaranteedReservation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["GR", "RC", "AR"]; example: "GR" |
| `cancellationPolicyProvidedInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `whatWasOrdered` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "What was ordered..." |
| `merchandiseWasCounterfeitDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `descCounterfeitMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Describe the counterfeit merchandise" |
| `descDispOfCounterfeitMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Describe the disposition of the counterfeit merchandise" |
| `originalCreditNotAccepted` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["R", "O"]; example: "R" |
| `explain` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explain" |
| `creditVoucherTransactionReceiptDated` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `creditVoucherOrTransactionReceiptDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cardholderCancelledReturnedMerchDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `merchantInLiquidationOrReceivershipInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `whatWasNotReceived` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "What was not received?" |
| `thirdPartyGiftCardInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `visaComCardVirtualAccInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `virtualAccFinancialLossInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `didMerchantCancelInd` | string | no | alid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchantCancellationDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `nonReceiptOfTravelServicesInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `disputeInvolveBondingAuthorityInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `explainAttemptToResolveWithBondAuth` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide an explanation of the attempt to resolve the dispute with the bonding authority/insurance scheme or where the information was obtained to confirm an insufficient bond/insurance scheme" |
| `bondAuthLetterOrAdviceDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `purchasedInfo` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide detailed description of what was purchased and an explanation of the dispute" |
| `expectedReceiptDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `expectedReceiptTime` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 25; example: "10:30" |
| `explainDisputePriorDeliveryDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explanation of dispute initiated prior to the expected delivery date" |
| `didCardholderCancelPriorExpectedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchandiseDeliveredWrongLocation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `lateDeliveryWrongLocation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide address of the agreed location or details of late delivery" |
| `didMerchantCancelMerchandiseInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchantCancelMerchandiseDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "What was ordered and how it was damaged" |
| `merchandiseReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cardholderMerchantPreviousNegotiationEvidence` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `whenNegotiationsBegin` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `explainPrevNegotiation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explain the previous ongoing negotiations between the cardholder and merchant." |
| `cardholderFirstNotifiedIssuerDisputeDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `serviceReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `howMerchandiseOrServiceMisrepresented` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "How was the merchandise or service misrepresented?" |
| `merchandiseServiceReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `explainPreNegotiation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "Explain the previous ongoing negotiations between the cardholder and merchant." |
| `orderDetailsNotAsDescribed` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide details of what was ordered and not as described" |
| `merchantReceivedReturnedMerchandiseDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `merchantAcceptCancellationInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `qualityOfFoodInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `purchasedInfoAndQualityIssue` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide information about what was purchased and the quality issue" |
| `didCardholderPayWorkRedone` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `howTermsOfContractNotHonoredByMerchant` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide details how the terms of the contract were either not honored by the merchant or not as described" |
| `nonFiatCurrencyNotDelivered` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchandiseDeliveredLate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchantInBankruptcyLiquidationInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `nonFiatCurrencyNotMatching` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `dispositionOfMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "a" |
| `merchantAcceptInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"] |
| `explainCreditIssuedLateDetailsOfNegotiations` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |

<!-- schema: #/components/schemas/PreArbitration -->
### Schema `PreArbitration`

Pointer: `#/components/schemas/PreArbitration`. Type: object (schema `PreArbitration`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `preArbReason` | string | yes | Pre-arbitartion reason | example: "Reason for pre-aritration" |
| `newInformationInd` | string | no | New information  - `Y` or `N` | enum: ["Y", "N"]; example: "Y" |
| `newInformationDescription` | string | no | New information description | example: "New information..." |
| `issuerCertifiesCardholderContactedInd` | string | no | Issuer certifies cardholder contact | enum: ["Y", "N"] |

<!-- schema: #/components/schemas/ClearingEloStructure -->
### Schema `ClearingEloStructure`

Pointer: `#/components/schemas/ClearingEloStructure`. Type: object (schema `ClearingEloStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transactionDestinationInstitutionIdCode` | string | no | Transaction destination institution ID code |  |
| `filePathMessageNumber` | string | no | File path message number |  |
| `additionalDataRecord` | object (schema `AdditionalDataRecordStructure`) | no |  |  |
| `authorizationCode` | string | no | Authorization code | example: "661810" |
| `caller` | string | no | Caller | example: "ELO" |
| `clearingType` | string | no | Clearing type | example: "CREDIT" |
| `correlationId` | string | no | Correlation IDentifier that links related API requests and events |  |
| `endpoint` | string | no | Endpoint | example: "000666" |
| `headerServiceFile` | object (schema `HeaderServiceFileStructure`) | no |  |  |
| `mainDataRecord` | object (schema `MainDataRecordStructure`) | no |  |  |
| `messageNumber` | string | no | Message number | example: "157" |
| `orgId` | string | no | Organization/tenant ID | example: "TN-41234404-7994-46d5-83d6-a55cxxxxxxxx" |
| `registrationFundsTransferData` | object (schema `RegistrationFundsTransferDataStructure`) | no |  |  |
| `registrationPaymentServiceData` | object (schema `RegistrationPaymentServiceDataStructure`) | no |  |  |
| `s3Path` | string | no | S3 path |  |
| `settlementCountryDataRecord` | object (schema `SettlementCountryDataRecordStructure`) | no |  |  |

<!-- schema: #/components/schemas/DisputeFormType -->
### Schema `DisputeFormType`

Pointer: `#/components/schemas/DisputeFormType`. Type: object (schema `DisputeFormType`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_form_type_id` | number | no | Unique id identification |  |
| `type` | string | no | Unique type identification |  |
| `description` | string | no | Generic description |  |

<!-- schema: #/components/schemas/DisputeFraudReportDocumentStructure -->
### Schema `DisputeFraudReportDocumentStructure`

Pointer: `#/components/schemas/DisputeFraudReportDocumentStructure`. Type: object (schema `DisputeFraudReportDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `acct_status` | string | yes | Account status | enum: ["ACCT_IS_OPEN", "ACCT_HAS_BEEN_CLOSED"]; example: "ACCT_IS_OPEN" |
| `chgbk_indicator` | string | yes | Is this a chargeback? true =  `1`, false = `0`. | enum: ["0", "1"]; example: "1" |
| `cvc_invalid_indicator` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-15-card-validation-code-cvc-indicator' target='_blank'>CVC invalid code indicator</a><br> | enum: ["Y", "*", "M", "N", "P", "U", "?", "E"]; example: "Y" |
| `device_type` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-3-account-device-type-codes' target='_blank'>account device type</a>.<br> | enum: ["1", "2", "3", "4", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]; example: "1" |
| `fraud_type` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-1-fraud-type-codes' target='_blank'>fraud type codes</a><br> | enum: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "51", "55", "56", "57"]; example: "00" |
| `report_date` | string | yes | Fraud report date, format = yyyy-mm-dd. | example: "2021-02-11" |
| `sub_type` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-2-fraud-sub-type-codes' target='_blank'>fraud sub type codes</a><br> | enum: ["K", "N", "P", "U"]; example: "K" |
| `authorization_origin_indicator` | string | no | Authorization origin indicator, default is null. **REQUIRED** for ELO network.<br><br>  `Y` - Issuer authorized<br><br>  `X` - Parameter authorized<br><br>  `N` - Not Authorized<br><br> | enum: ["Y", "X", "N"]; minLength: 1; maxLength: 1; nullable: true; example: "Y" |
| `notification_code` | string | no | Notification type code. Default is null. **REQUIRED** for ELO network.<br><br>  `1` - First notification<br><br>  `2` - Notification sent again<br><br>  `3` - Change<br><br>  `4` - Deletion (cancellation fraud warning)<br><br>  `5` = Reactivation<br><br> | enum: ["1", "2", "3", "4", "5"]; minLength: 1; maxLength: 1; nullable: true; example: "1" |
| `exchange_indicator` | string | no | Is this an exchange? Default is `N`. **REQUIRED** for ELO network.<br><br>  `Y` - Yes<br><br>  `N` - No<br><br> | enum: ["N", "Y"]; minLength: 1; maxLength: 1; example: "N" |
| `exchange_value` | number | no | Exchange value. **REQUIRED** for ELO network. | example: 9.99 |
| `card_service_code` | string | no | Card type. **REQUIRED** for ELO network.<br><br>  `C` - Chip<br><br>  `M` - Stripe<br><br> | enum: ["C", "M"]; minLength: 1; maxLength: 1; example: "C" |

<!-- schema: #/components/schemas/CardholderVerificationMethodStructure -->
### Schema `CardholderVerificationMethodStructure`

Pointer: `#/components/schemas/CardholderVerificationMethodStructure`. Type: object (schema `CardholderVerificationMethodStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `onlinePIN` | string | no | Online PIN Preferring. PIN preferring means that verficiation will first ask for a PIN.<br><br>Valid Values/Format: 1 | maxLength: 1; example: "1" |
| `offlinePIN` | string | no | Offline PIN.<br><br> Valid Values/Format: 2 | maxLength: 1; example: "2" |
| `signature` | string | no | Signature<br><br>Valid Values/Format: 3 | maxLength: 1; example: "3" |
| `none` | string | no | None (No Cardholder Verfication Method)<br><br>Valid Values/Format: 4 | maxLength: 1; example: "4" |

<!-- schema: #/components/schemas/AdditionalDataRecordStructure -->
### Schema `AdditionalDataRecordStructure`

Pointer: `#/components/schemas/AdditionalDataRecordStructure`. Type: object (schema `AdditionalDataRecordStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `airportTaxValue` | string | no | Airport tax Value - Registry 01 - Field 37 | example: "000000000000" |
| `changeValue` | string | no | Change Value - Registry 01 - Field 46 | example: "00000000000" |
| `codeProduct` | string | no | Code Product - Registry 01 - Field 33 | example: "071" |
| `conditionalCodeChipTransaction` | string | no | Conditional code chip Transaction - Registry 01 - Field 47 | example: "0, 1, 2" |
| `cpfOrCnpj` | string | no | CPF or CNPJ - Registry 01 - Field 45 | example: "00000000000000" |
| `feePaymentInput` | string | no | Fee payment input - Registry 01 - Field 43 | example: "00000" |
| `indicatorMovement` | string | no | Indicator Movement - Registry 01 - Field 40 | example: "0" |
| `installmentNumber` | string | no | Installment Number - Registry 01 - Field 42 | example: "000" |
| `logicalNumberEquipment` | string | no | Logical Number Equipment - Registry 01 - Field 36 | example: "20172289" |
| `numberInstallmentsTransaction` | string | no | Number Installments Transaction - Registry 01 - Field 41 | example: "000" |
| `pointOfSale` | string | no | Point of sale - Registry 01 - Field 35 | example: "000000000000001" |
| `referenceNumberDispute` | string | no | Reference Number Dispute - Registry 01 - Field 30 | example: "000000" |
| `transactionCode` | string | no | Transaction Code - Registry 01 - Field 01 | example: "06" |
| `transactionIndicator` | string | no | Transaction Indicator - Registry 01 - Field 38 | example: "8" |
| `transactionSubCode` | string | no | Transaction SubCode - Registry 01 - Field 02 | example: "01" |
| `transactionValue` | string | no | Transaction Value - Registry 01 - Field 39 | example: "000000000000" |
| `walletId` | string | no | Wallet Id - Registry 01 - Field 28 | example: "00000000000" |

<!-- schema: #/components/schemas/HeaderServiceFileStructure -->
### Schema `HeaderServiceFileStructure`

Pointer: `#/components/schemas/HeaderServiceFileStructure`. Type: object (schema `HeaderServiceFileStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `codeAcquirer` | string | no | Code acquirer - Registry B0 - Field 13 | example: "0000" |
| `codeProcessor` | string | no | Code processor - Registry B0 - Field 11 | example: "3178" |
| `emittingBank` | string | no | Emitting bank - Registry B0 - Field 10 | example: "0985" |
| `fileVersion` | string | no | File version - Registry B0 - Field 16 | example: "231" |
| `flagCode` | string | no | Flag code - Registry B0 - Field 14 | example: "007" |
| `futureUse2` | string | no | Future use - Registry B0 | example: "0" |
| `returnDateArchive` | string | no | Return date archive - Registry B0 - Field 08 | example: "00000000" |
| `returnTimeArchive` | string | no | Return time archive - Registry B0 - Field 09 | example: "000000" |
| `routeIndicatorArchive` | string | no | Route indicator archive - Registry B0 - Field 15 | example: "1" |
| `sendDate` | string | no | Send date - Registry B0 - Field 06 | example: "20230717" |
| `serviceCode` | string | no | Service code - Registry B0 - Field 02 | example: "10" |
| `shipmentNumber` | string | no | Shipment number - Registry B0 - Field 04 | example: "0177" |
| `shippingDate` | string | no | Shipping date - Registry B0 - Field 03 | example: "20230717" |
| `shippingTimeArchive` | string | no | Shipping time archive - Registry B0 - Field 07 | example: "152300" |
| `transactionSubCode` | string | no | Transaction sub code - Registry B0 - Field 01 | example: "B0" |
| `windowNumber` | string | no | Window number - Registry B0 - Field 05 | example: " " |

<!-- schema: #/components/schemas/MainDataRecordStructure -->
### Schema `MainDataRecordStructure`

Pointer: `#/components/schemas/MainDataRecordStructure`. Type: object (schema `MainDataRecordStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorizationOrCancellationOriginIndicator` | string | no | Authorization or cancellation origin indicator - Registry 00 - Field 06 | example: "1" |
| `cardholderVerificationMethod` | string | no | Cardholder verification method - Registry 00 - Field 24 | example: "1" |
| `cardNumber` | string | no | Card number - Registry 00 - Field 03 |  |
| `codeAcquirer` | string | no | Code acquirer - Registry 00 - Field 08 | example: "9000" |
| `codeAuthorizationTransaction` | string | no | Code authorization transaction - Registry 00 - Field 22 | example: "661810" |
| `codeCurrency` | string | no | Code currency - Registry 00 - Field 12 | example: "986" |
| `codeFlag` | string | no | Code flag - Registry 00 - Field 19 | example: "007" |
| `codeReasonDispute` | string | no | Code reason dispute - Registry 00 - Field 21 | example: "00" |
| `futureUse2` | string | no | Future use2 - Registry 00 | example: "00" |
| `futureUse4` | string | no | Future use4 - Registry 00 | example: "0" |
| `futureUse5` | string | no | Future use5 - Registry 00 | example: "0000" |
| `identificationTransaction` | string | no | Identification transaction - Registry 00 - Field 20 | example: "1" |
| `numberReferenceTransaction` | string | no | Number reference transaction - Registry 00 - Field 07 | example: "70090003198000000723318" |
| `pointOfSaleCity` | string | no | Point of sale city - Registry 00 - Field 14 | example: "ZAMBAS" |
| `pointOfSaleCountryCode` | string | no | Point of sale country code - Registry 00 - Field 15 | example: "BR" |
| `pointOfSaleMcc` | string | no | Point of sale mcc - Registry 00 - Field 16 | example: "6531" |
| `pointOfSaleName` | string | no | Point of sale name - Registry 00 - Field 13 | example: "Lns" |
| `posEntryMode` | string | no | Pos entry mode - Registry 00 - Field 26 | example: "07" |
| `processCode` | string | no | Process code - Registry 00 - Field 131 | example: "53" |
| `processingDate` | string | no | Processing date - Registry 00 - Field 27 | example: "20230717" |
| `sellValue` | string | no | Sell value - Registry 00 - Field 11 | example: "000000001000" |
| `terminalCapability` | string | no | Terminal capability - Registry 00 - Field 23 | example: "V" |
| `transactionCode` | string | no | Transaction code - Registry 00 - Field 01 | example: "06" |
| `transactionDate` | string | no | Transaction date - Registry 00 - Field 09 | example: "20230717" |
| `transactionSubCode` | string | no | Transaction subCode - Registry 00 - Field 02 | example: "00" |
| `transactionTime` | string | no | Transaction time - Registry 00 - Field 10 | example: "092225" |

<!-- schema: #/components/schemas/RegistrationFundsTransferDataStructure -->
### Schema `RegistrationFundsTransferDataStructure`

Pointer: `#/components/schemas/RegistrationFundsTransferDataStructure`. Type: object (schema `RegistrationFundsTransferDataStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cardBIN` | string | no | Card BIN - Registry 03 - Field 137 | example: "00000000" |
| `identificationNumberOfPersonImpacted` | string | no | Identification number of person impacted - Registry 03 - Field 133 | example: "18230565371336" |
| `last4DigitsCard` | string | no | Last 4 digits card - Registry 03 - Field 143 | example: "0000" |
| `nameCarrier` | string | no | Name carrier - Registry 03 - Field 134 | example: "bR1YsI xhDVQNL" |
| `originFunds` | string | no | Origin funds - Registry 03 - Field 138 | example: "02" |
| `phoneCarrier` | string | no | Phone carrier - Registry 03 - Field 136 | example: "00000000000" |
| `transactionCode` | string | no | Transaction code - Registry 03 - Field 01 | example: "06" |
| `transactionSubCode` | string | no | transactionSubCode - Registry 03 - Field 02 | example: "P2P" |
| `typePayment` | string | no | Type payment - Registry 03 - Field 132 | example: "06" |

<!-- schema: #/components/schemas/RegistrationPaymentServiceDataStructure -->
### Schema `RegistrationPaymentServiceDataStructure`

Pointer: `#/components/schemas/RegistrationPaymentServiceDataStructure`. Type: object (schema `RegistrationPaymentServiceDataStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amountAuthorized` | string | no | Amount authorized - Registry 05 - Field 72 | example: "000000001000" |
| `codeAnswerAuthorization` | string | no | Code answer authorization - Registry 05 - Field 132 | example: "00" |
| `codeCurrencyValueAuthorized` | string | no | Code currency value authorized - Registry 05 - Field 64 | example: "986" |
| `futureUse19` | string | no | Future use 19 - Registry 05 - Field 70 | example: "00" |
| `identifierTransaction` | string | no | Identifier transaction - Registry 05 - Field 61 | example: "202289723318" |
| `indicatorBusinessElectronic` | string | no | Indicator business electronic - Registry 05 - Field 69 | example: "00" |
| `transactionCode` | string | no | Transaction code - Registry 05 - Field 01 | example: "06" |
| `transactionSubCode` | string | no | Transaction subCode - Registry 05 - Field 99 | example: "05" |
| `valueAuthorized` | string | no | Value authorized - Registry 05 - Field 62 | example: "000000001000" |

<!-- schema: #/components/schemas/SettlementCountryDataRecordStructure -->
### Schema `SettlementCountryDataRecordStructure`

Pointer: `#/components/schemas/SettlementCountryDataRecordStructure`. Type: object (schema `SettlementCountryDataRecordStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `countryCodeSettlement` | string | no | Country code settlement - Registry 02 - Field 50 | example: "BR" |
| `dateLiquidationTransaction` | string | no | Date liquidation transaction - Registry 02 - Field 139 | example: "20230718" |
| `dateMovementTransactionOriginal` | string | no | Date movement transaction original - Registry 02 - Field 54 | example: "00000000" |
| `municipalCode` | string | no | Municipal code - Registry 02 - Field 146 | example: "0000000" |
| `networkReferenceId` | string | no | Network reference id - Registry 02 - Field 145 | example: "1982391A0020319" |
| `pointOfSaleMarketplaceCode` | string | no | Point of sale marketplace code - Registry 02 - Field 140 | example: "000000000000000" |
| `quantityDaysFinancialTransaction` | string | no | Quantity days financial transaction - Registry 02 - Field 52 | example: "001" |
| `transactionCode` | string | no | Transaction code - Registry 02 - Field 01 | example: "06" |
| `transactionSubCode` | string | no | Transaction subCode - Registry 02 - Field 02 | example: "02" |
| `valueExchange` | string | no | Value exchange - Registry 02 - Field 53 | example: "0000000000" |
| `zipCodeEstablishmentCommercial` | string | no | Zip code establishment commercial - Registry 02 - Field 81 | example: "i7qQFhLh" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `Supporting forms`: POST /v1/disputes/{disputeId}/forms, PUT /v1/disputes/{disputeId}/forms/{disputeFormId}, POST /v1/disputes/{disputeId}/fraud-report, PUT /v1/disputes/{fraudReportId}/fraud-report | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-visa-colloboration-questionaire-part-01` — Visa collaboration and allocation questionnaires (part 1 of 7)
- `KU-EVT-disputes-endpoint-generated-events` — Card issuing - Disputes
