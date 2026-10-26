---
ku_id: KU-PAY-pix-automatic
title: Pix Automatic
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/pix-automatic.md
  sha256: 6d7c5504f24242b8bea7ea7a854611d11723d4d9a702026fa316a8f8af59846b
  url: https://developers.pismo.io/pismo-docs/docs/pix-automatic
  role: primary_guide
  updated_at: '2026-04-24T22:32:06.000Z'
operations:
- accept-reject-authorization
- cancel-automatic-pix-payment-order
- cancel-recurrence-automatic
- post-create-recurrence-cob
- post-pix-out-transfer
- post-qr-code
- post-recurrence-automatic
- post-schedule-pix-payment
- update-order-automatic-pix
- update-recurrence-automatic
related_kus:
- KU-API-instant-payments-automatic-pix--automatic-pix
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-qr-code--recurring-payment
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
grouping_rationale: single source page
---

# Pix Automatic

**KU ID:** `KU-PAY-pix-automatic` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/pix-automatic.md`:

> The Central Bank of Brazil (BACEN) created **Pix Automatic** - a Pix (Brazilian instant payment system) feature that allows for scheduled and automatic recurring transfers. Customers that make recurring payments, such as subscriptions, school fees, rent, and more, will find this feature useful.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/pix-automatic.md`: Pix Automatic; Key features; Benefits; Scheduled transfers versus Pix Automatic; Pix Automatic use cases (journeys); Journey flows; Step 1—Payee initiates recurrence request; Step 2—Payer receives request; Step 3—Payer acknowledges the recurrence request (it's automatically done by Pismo ); Step 4— Pismo notification; Step 5 —Payer confirms or rejects recurrence; Step 6—Payee receive payer’s confirmation; Step 1—Receiver generates recurrence; Step 2—Payer reads the QR Code; Step 3—Pismo creates recurrence for the payer; Step 4—Payer accepts recurrence; Step 1—Receiver generates recurrence with composite QR Code; Step 2—Payer reads the QR Code; Step 3—Payer executes immediate payment; Step 4—Pismo receives payment confirmation; Step 5—Payer accepts the recurrence; Step 1—Receiver creates recurrence with charge; Step 2—Payer reads the QR Code; Step 3—Payer completes or schedules payment; Step 4—Payer accepts the recurrence; Pix Automatic transaction flow; Step 1 - Merchant sends payment recurrence request; Step 2 - Customer receives authorization request; Step 3 - Customer authorizes payment; Step 4 - Recurring payments executed automatically; Step 5 - Notifications sent; Recurrence value types; Updating recurrence values; Payment order workflow; Receiver flow; Payer flow; Acceptance and scheduling; Recurrence cancellation; Payer-side behavior; Receiver-side behavior; Payment order execution and retry; Due data execution; Failure handling; Retry flows; Payment order cancellation; Step 1 - Recurrence creation; Step 2 - Sending the recurrence request; Step 3 - Acknowledgment and validation; Step 4 - Payer notification; Step 5 - Payer authorization; Step 6 - Payment Instruction sent; Step 7 - Payer validates payment Instruction; Step 8 - Scheduling the transactions; Step 9 - Transaction execution

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/pix-automatic.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/pix-automatic · updatedAt: 2026-04-24T22:32:06.000Z

<!-- source:begin path=docs/core-banking/pix-automatic.md part=0-end -->

# Pix Automatic

The Central Bank of Brazil (BACEN) created **Pix Automatic** - a Pix (Brazilian instant payment system) feature that allows for scheduled and automatic recurring transfers. Customers that make recurring payments, such as subscriptions, school fees, rent, and more, will find this feature useful.

With Pix Automatic, you can define a specific amount and frequency (daily, weekly, monthly, and so on.) so that the transfer is automatically executed on a scheduled date without the need for a manual transaction. This automation  facilitates financial management and payment punctuality.

PIX Automatic is expected to replace many use cases that boletos and traditional direct debit systems currently handle, making the payments landscape in Brazil more efficient, user-friendly, and digital-native.

Pismo provides a full set of [API endpoints](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic)   to implement this feature.

## Key features

* **Automatic and recurring payments**—Allows users to authorize merchants or service providers to automatically charge them on a scheduled basis—perfect for things like subscriptions, utility bills, or loan repayments.
* **Pre-authorization**—Payer gives one-time consent for future payments. After that, the merchant can initiate charges at agreed-upon intervals.
* **Real-time settlement**—Just like regular Pix, funds move instantly—except now it happens without manual approval each time.
* **24/7 availability**—Payments can be processed anytime, even on weekends and holidays.
* **Security and transparency**—All charges are clearly displayed to the user, with options to review, cancel authorization, or limit payment amounts/frequency.

## Benefits

* **For consumers**—No missed payments, more control than traditional direct debits.
* **For businesses**—Predictable cash flow, lower transaction costs than cards, reduced churn.
* **For banks/fintechs**—New revenue models via value-added services and better customer engagement.

# Scheduled transfers versus Pix Automatic

|                     | Payment type                                                                      | Nature                                                                                                    | Amount            | Common uses                        | Participants                                                                                      |
| :------------------ | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :---------------- | :--------------------------------- | :------------------------------------------------------------------------------------------------ |
| Scheduled transfers | Payer initiates recurring scheduled Pix (push payment)                            | Automatic recurrence created based on the payer's instructions                                            | Fixed             | General Pix payments               | Either a natural person (individual) or a legal person (corporation or organization) can initiate |
| Pix Automatic       | Payee initiates Automatic Pix after obtaining payer authorization (pull payment). | Automatic recurring transfer based on prior authorization from the payer, with payee payment instructions | Fixed or variable | Purchases or business transactions | Legal person (corporation or organization) can initiate                                           |

<br />

# Pix Automatic use cases (journeys)

The following uses cases are referred to as ***journeys*** in the official Pix Automatic documentation.

| Journey | Use case                                                       | Description                                                                                                                                                                                                                                                                      | Code enum |
| :------ | :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| 1       | Pix Automatic request via API                                  | Bank notification. If the merchant has the payer's banking information, a push notification can be sent directly to the payer's bank app, prompting them to authorize the recurring payment.                                                                                     | `AUT1`    |
| 2       | QR Code for recurring payment authorization                    | Authorization via QR code. Payer scans a merchant provided QR code to authorize recurring payments. This method does not initiate an immediate payment, allowing the first payment to be scheduled for a later date.                                                             | `AUT2`    |
| 3       | QR Code for recurring payment authorization with first payment | Authorization via QR code with first payment. Similar to the second method, but the QR code includes information for both the authorization and the initial payment, enabling the payer to authorize the recurring payment and make the first payment in a single step.          | `AUT3`    |
| 4       | QR Code for immediate payment with sign-up option              | Post-payment sign-up path. After completing a one-time payment via QR code, the payer is offered the option to authorize recurring payments for future transactions. This involves a composite QR Code (one location for payment + one location for subscription authorization). | `AUT4`    |

## Journey flows

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Journey one flow</summary>

  Journey one is a  direct API Request using `authorization_id`. The receiver exclusively initiates this journey via API that sends a recurrence request to the Payer. It is identified by `authorization_id` and `recurrence_id`.

  ### Step 1—Payee initiates recurrence request

  Payee initiates recurrence request via [Create recurrence](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic) (POST /v1/pix/automatic).

  Payee events generated:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-status-change-1">Pix recurrence status changed</a>, `status` =  `CREATED`.
  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `CREATED`

  ### Step 2—Payer receives request

  Payer events generated:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-status-change-1">Pix recurrence status changed</a>, `status` =  `CREATED`.
  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `CREATED`

  ### Step 3—Payer acknowledges the recurrence request (it's automatically done by Pismo )

  Payer events generated:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `RECEIVED`

  Payee events generated:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `RECEIVED`

  ### Step 4— Pismo notification

  A notification must be delivered for the paying user asking for confirmation or rejection of the\
  recurrence—<a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `RECEIVED`

  if the payer does not answer until the expiration date the recurrence request will\
  automatically expired.

  Payer generated event:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `EXPIRED`

  Payee generated event:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `EXPIRED`

  ### Step 5 —Payer confirms or rejects recurrence

  Payer confirms or rejects recurrence— [Accept/reject recurrence authorization](https://developers.pismo.io/pismo-docs/reference/accept-reject-authorization)  (POST /v1/pix/automatic/payer/authorization).

  Payer generated events:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-status-change-1">Pix recurrence status changed</a>, `status`=  `ACCEPTED` or `REJECTED`
  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `ACCEPTED` or `REJECTED`

  Payee generated events:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-status-change-1">Pix recurrence status changed</a>, `status`=  `ACCEPTED` or `REJECTED`
  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-authorization-status-change-1">Pix recurrence authorization status changed</a>, `status`= `ACCEPTED` or `REJECTED`

  ### Step 6—Payee receive payer’s confirmation

  Payee generated events:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-status-change-1">Pix recurrence status changed</a>, `status`=  `APPROVED`

  Payer generated events:

  * <a href="https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-status-change-1">Pix recurrence status changed</a>, `status`=  `APPROVED`
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Journey two flow</summary>

  Journey 2 – QR Code with COBR (no prior payment). The Receiver generates a QR Code containing only a COBR location. The Payer reads the QR Code and accepts the recurrence. No payment is required upfront.

  ### Step 1—Receiver generates recurrence

  Payer accepts recurrence with QR Code [Create recurrent COB QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cob)(POST

  /qrcode/v1/pix/qrcode/recurrence).

  ### Step 2—Payer reads the QR Code

  Payer reads the QR code [Validate QR Code](https://developers.pismo.io/pismo-docs/reference/post-qr-code)(POST /pix/v1/pix/qrcode/validate).

  ### Step 3—Pismo creates recurrence for the payer

  Pismo creates recurrence for the payer (`status` = `WAITING_DEFINITION`).

  ### Step 4—Payer accepts recurrence

  Payer accepts recurrence via [Accept/reject recurrence authorization](https://developers.pismo.io/pismo-docs/reference/accept-reject-authorization) (POST /v1/pix/automatic/payer/authorization)
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Journey three flow</summary>

  Journey 3 – QR Code with COB + COBR (mandatory payment). The Receiver generates a QR Code with two locations:

  1. COB (immediate payment)
  2. COBR (recurrence proposal)

  The Payer must successfully complete the COB payment to activate the COBR recurrence. If either location is invalid, the process fails.

  ### Step 1—Receiver generates recurrence with composite QR Code

  Receiver generates recurrence with composite QR Code—[Create recurrent COB QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cob)  (POST /qrcode/v1/pix/qrcode/cob/recurrence).

  ### Step 2—Payer reads the QR Code

  Payer reads the QR Code—[Validate QR Code](https://developers.pismo.io/pismo-docs/reference/post-qr-code)  (POST /pix/v1/pix/qrcode/validate).

  ### Step 3—Payer executes immediate payment

  Payer executes immediate payment—[Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer)  (POST /pix/v1/pix/out/transfer).

  ### Step 4—Pismo receives payment confirmation

  Pismo receives payment confirmation—[Pix-out notification received](https://developers.pismo.io/events/docs/pix-pix-out-1)

  ### Step 5—Payer accepts the recurrence

  Payer accepts the recurrence via [Accept/reject recurrence authorization](https://developers.pismo.io/pismo-docs/reference/accept-reject-authorization)  POST /v1/pix/automatic/payer/authorization
</details>

<details>
  <summary style={{ fontSize: "20px", fontWeight: "bold" }}>Journey four flow</summary>

  <br />

  Journey 4 – Offer after payment (COBV or static). The Receiver generates a QR Code containing either a COBV (charge without due date) or a static charge + COBR. The Payer reads the QR Code and may accept the recurrence after completing or scheduling the payment.

  ### Step 1—Receiver creates recurrence with charge

  Receiver creates recurrence with charge (COBV or Static).

  ### Step 2—Payer reads the QR Code

  Payer reads the QR Code—[Validate QR Code](https://developers.pismo.io/pismo-docs/reference/post-qr-code) (POST /pix/v1/pix/qrcode/validate).

  ### Step 3—Payer completes or schedules payment

  Payer completes or schedules payment—[Schedule transfer](https://developers.pismo.io/pismo-docs/reference/post-schedule-pix-payment)  (POST /pix/v1/pix/out/transfer or /pix/v2/pix/out/scheduler).

  ### Step 4—Payer accepts the recurrence

  Payer accepts the recurrence via [Accept/reject recurrence authorization](https://developers.pismo.io/pismo-docs/reference/accept-reject-authorization)( POST /v1/pix/automatic/payer/authorization)
</details>

# Pix Automatic transaction flow

The following is a simplified flow for a typical Pix Automatic transaction.

### Step 1 - Merchant sends payment recurrence request

The merchant (e.g., gym, streaming service) initiates a [recurring payment request](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic)  to the customer’s bank.

Request includes the following:

* Payer identification and data
* Receiver Identification and data
* Payment amount
* Frequency (daily, weekly, monthly, and so on)
* Automatic transactions start date and, if necessary, end date.

### Step 2 - Customer receives authorization request

The customer is notified via their banking app to authorize the recurring payment.

### Step 3 - Customer authorizes payment

Upon reviewing the details, the customer [approves the recurring payment](https://developers.pismo.io/pismo-docs/reference/accept-reject-authorization)   agreement.

### Step 4 - Recurring payments executed automatically

On the agreed dates, payments are automatically debited from the customer’s account and credited to the merchant, without further action needed from the customer.

### Step 5 - Notifications sent

Both the customer and merchant receive confirmations for each successful transaction.

# Recurrence value types

Pix Automatic supports two billing configurations for recurrences types: fixed amount and variable amount. The receiver defines the type at [recurrence creation time](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic)  using the `dynamic_amount` parameter.

**Fixed amount**

* `dynamic_amount` = `false`
* The Receiver must specify the exact recurrence value using the `amount` field.  The `amount` value is used for recurrences

**Variable amount**

* `dynamic_amount` = `true`
* The Receiver must define a `min_payment_amount` (minimum amount per charge).
* The Payer, during recurrence acceptance, just define a `max_payment_amopunt` (minimum amount they are willing to pay per change).
* If the payer does not specify a maximum amount, then there is no upper limit for accepting payment orders.

## Updating recurrence values

To update a recurrence's minimum and maximum values, call the [Update automatic recurrence ](https://developers.pismo.io/pismo-docs/reference/update-recurrence-automatic) (PATCH /v1/pix/automatic/\{recurrence\_id}) endpoint.

**Notes:**

* The Receiver can update the minimum amount (`min_payment_amount`) only before the recurrence is accepted.
* The Payer can update the maximum amount )`max_payment_amount`) at anytime, even after acceptance.

# Payment order workflow

<Image align="center" src="https://files.readme.io/04f4b9a7ec729e4684d1a00eeb5cb9e6111929f92e28cc5a57454e33d3ed4253-Payment_Order_Workflow_Diagram_1.png" />

Payment order process:

1. Receiver’s payment service provider (PSP) sends payment instructions to the payer’s PSP.
2. Between 10 and 2 days before the due date, the payer receives this order and performs validations.
3. Once accepted, the payment is scheduled for execution on the due date.

The payer's authorization is required in the recurring with authorization flow. Once authorized, the recurrence automatically generate payment orders.

There are two distinct flows for payment orders: Payer and Receiver.

## Receiver flow

In the Receiver flow, behavior depends on the recurrence value type:

* **Fixed value**—The payment order is generated and sent immediately. This generates a  [Pix recurrence payment order status changed](https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-payment-order-status-change-1)  event.
* **Variable value**
  * Pismo generates the payment order and sends it to the receiver client, who must then pass the actual payment amount using the [Update payment order amount](https://developers.pismo.io/pismo-docs/reference/update-order-automatic-pix) endpoint. This generates a  [Pix recurrence payment order status changed](https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-payment-order-status-change-1)  event with `status` = `WAITING_CUSTOMER`.
  * Pismo waits for the receiver to send the amount via [Update payment order amount](https://developers.pismo.io/pismo-docs/reference/update-order-automatic-pix).

## Payer flow

In the Payer flow, when Pismo receives the payment order, it performs validations to determine whether to:

* Accept the order and schedule the payment execution, or
* Reject the instruction and notify the receiver’s PSP.

<details>
  <summary style={{ fontWeight: "bold", fontSize: "18px" }}>Rejection conditions and error codes</summary>

  **Rejection conditions**

  * Authorizations expired or does not exist
  * Authorization was cancelled
  * Fixed amount mismatch
  * Variable amount exceeds maximum
  * Duplicate charge for same cycle
  * Receiver mismatch
  * Instruction outside scheduling window (2-10 days before due date)

  **Error codes for instruction validation**

  * AC06 - Payer's transactional account blocked
  * AM02 - Charge amount exceeds authorized maximum
  * AM09 - Charge amount does not match recurrence
  * DENC - Payer CPF/CNPJ mismatch
  * DTED - Due date conflicts with recurrence rules
  * DTNT - Post-due attempts exceed D+8
  * FBRD - Pain.013 received outside business window
  * IRNT - Recurrence does not allow post-due retries
  * MIDI - Invalid or nonexistent recurrence ID
  * MSUC - Recurrence not confirmed by payer
  * NIEC - Duplicate payment order already pending
  * NIPA - Payment already completed
  * NITX - Instruction does not match previous charge
  * QUNT - More than 3 retries in 7 days after due date
  * UDEI - Invalid payer CPF/CNPJ
</details>

### Acceptance and scheduling

Once accepted, Pismo schedules for payment and generates a  [Pix recurrence payment order status changed](https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-payment-order-status-change-1)  event with `status` = `ACTIVE` or `REJECTED`. The Receiver's PSP also receives this event.

## Recurrence cancellation

Both the Payer and Receiver can cancel a recurrence via the [Cancel recurrence](https://developers.pismo.io/pismo-docs/reference/cancel-recurrence-automatic) (POST /v1/pix/automatic/cancel) endpoint. This endpoint generates a  [Pix recurrence payment order status changed](https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-payment-order-status-change-1)  event with `status` = `CANCELLED` and includes the cancellation reason (`reason`object) .

### Payer-side behavior

* Pismo checks for active scheduled payments linked to the recurrence
* If a payment is scheduled for a future date (`due_date` greater than today), it is automatically cancelled
* If a payment is scheduled for today (`due_date` = today), it executes normally

### Receiver-side behavior

* Pismo automatically cancels all future payment orders
* Payment orders scheduled for today are still executed

## Payment order execution and retry

### Due data execution

On the due date, Pismo attempts payment between 00:00 and 08:00 (Brasilia time). If successful the payer's PSP receives the [Pix recurrence payment order status changed](https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-payment-order-status-change-1)  event with `status` = `CONCLUDED` and a Pix-out configuration.

### Failure handling

If failure occurs before reaching the provider (i.e., insufficient funds)

* Pismo retries between 18:00 and 21:00
* No further attempts after 21:00

If failure occurs before reaching the provider (i.e., SPI (Brazil instant payment system) rejects reused `end_to_end_ID`)

* Pismo cancels the order and generates the [Pix recurrence payment order status changed](https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-payment-order-status-change-1)   event with `status` = `CANCELLED`
* To proceed with a new payment attempt, Pismo generates, for the Receiver's PSP, a new payment instruction using a new `end_to_end_ID`, since the SPI does not allow previously submitted identifier reuse.

### Retry flows

Post-due retry (`RETRY_OVERDUE`, SPI code `NTAG`)

* Triggered if payment not complete by 21:00
* Pismo checks retry eligibility and generates new order for D+2

Intra-day retry (`RETRY_FAILUER`, SPI code: `RFIL`)

* Triggered when Receiver's PSP gets cancellation with reason `FAIL`
* New order is generated for same settlement day

### Payment order cancellation

Payment orders can be cancelled in two ways:

1. Pismo automatically cancels due to recurrence cancellation
2. Payer or Receiver manually cancels via the [Cancel payment order](https://developers.pismo.io/pismo-docs/reference/cancel-automatic-pix-payment-order) (POST /v1/pix/automatic/payment/order/cancel) endpoint. This generates the [Pix recurrence payment order status changed](https://developers.pismo.io/events/docs/instantpay-pullpayments-pix-recurrence-payment-order-status-change-1)   event with `status` = `CANCELLING`. After the counterparty confims the cancellation, the same event is generated with `status` = `CANCELLED`.

**Note:** Payment order cancellations are only allowed up to 24 hours before the due date.

**Special case: Reason fail**

If the cancellation reason is `FAIL`, Pismo may initiate an intra-day payment order retry within the Receiver-side flow using a new `end_to_end_ID`and a `RETRY_FAILURE` retry type.

<details>
  <summary style={{ fontSize: "24px" }}>
    <b> Pix Automatic  receiver process for use case #1</b>
  </summary>

  ### Step 1 - Recurrence creation

  Receiver [configures the details](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic)   for the recurrence they wish to establish in their system:

  * Payer identification and data
  * Receiver Identification and data
  * Payment amount
  * Frequency (daily, weekly, monthly, etc.)
  * Automatic transactions start date and, if necessary, end date

  ### Step 2 - Sending the recurrence request

  * Receiver calls the financial institution's API endpoint to send the recurrence request. The request includes all the details configured in the receiver's system.
  * Financial institution validates the recurrence data.

  ### Step 3 - Acknowledgment and validation

  * Financial institution validates the recurrence request data.
  * After validation, the financial institution responds with an acknowledgment to the receiver, confirming that the message has been received.
  * Payer updates the recurrence status to  "Awaiting Approval" or "Rejection".

  ### Step 4 - Payer notification

  * Financial institution sends a notification to the payer via a webhook with the details of the recurrence request.
  * Payer receives the notification (via banking app, SMS, etc.) and reviews the request details.

  ### Step 5 - Payer authorization

  * [Payer authorizes or rejects the recurrence](https://developers.pismo.io/pismo-docs/reference/accept-reject-authorization)  (Link to Authorization endpoint).
  * Financial institution updates the recurrence status based on the payer's action.
  * Via event streams, the receiver sees status changes notifications

  ### Step 6 - Payment Instruction sent

  Between 10 to 2 days before the due date, the receiver's financial institution sends a payment instruction to the payer's institution, confirming the scheduled transfer's details.

  ### Step 7 - Payer validates payment Instruction

  * Payer must validate the payment instruction according to the previously given authorization data.
  * If the payment instruction does not match, the payer must reject it.
  * The financial institution notifies the receiver about the validation or rejection of the payment instruction.

  ### Step 8 - Scheduling the transactions

  Based on the validated and received payment instruction, the payer's institution schedules the recurring transfers.\
  On the scheduled date, the financial institution's system automatically transfers the defined amount from the payer's account to the receiver's account.

  ### Step 9 - Transaction execution

  The receiver receives notifications via webhooks or API queries about the execution of transfers.\
  Each status change is notified to the receiver through event streams.
</details>

<br />

\*/}
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /inst-pull-pay/v1/pix/automatic` | `post-recurrence-automatic` | Create recurrence | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /inst-pull-pay/v1/pix/automatic/payer/authorization` | `accept-reject-authorization` | Accept/reject recurrence authorization | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /v1/pix/qrcode/cob/recurrence` | `post-create-recurrence-cob` | Create recurrent COB QR Code | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /pix/v1/pix/qrcode/validate` | `post-qr-code` | Validate QR Code | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | Schedule transfer(s) V2 | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `PATCH /inst-pull-pay/v1/pix/automatic/{recurrence_id}` | `update-recurrence-automatic` | Update automatic recurrence | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `PATCH /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}` | `update-order-automatic-pix` | Update payment order amount | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /inst-pull-pay/v1/pix/automatic/cancel` | `cancel-recurrence-automatic` | Cancel recurrence | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /inst-pull-pay/v1/pix/automatic/payment/order/cancel` | `cancel-automatic-pix-payment-order` | Cancel payment order | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |

### Operation essentials

- **`POST /inst-pull-pay/v1/pix/automatic`** (`post-recurrence-automatic`): security not declared; required parameters `x-account` (header), `Idempotency-Key` (header); required body fields `contract_id`, `description`, `frequency_type`, `allow_attempts_after_expiration`, `first_payment_date`, `debtor`, `payer`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /inst-pull-pay/v1/pix/automatic/payer/authorization`** (`accept-reject-authorization`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `recurrence_id`, `status`, `journey_type`; response statuses 201, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /v1/pix/qrcode/cob/recurrence`** (`post-create-recurrence-cob`): security not declared; required parameters `Authorization` (header); required body fields `payee`, `payer`, `initial_amount`, `transaction_identification`; response statuses 202, 400, 401, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events none listed.
- **`POST /pix/v1/pix/qrcode/validate`** (`post-qr-code`): security not declared; required parameters `Authorization` (header); required body fields `emv`; response statuses 200, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0003`, `EPIX0015`, `EPIX0019`, `EPIX0020`, `PCE001`, `EPIX0032`, `EPIX0061`, `EPIX0070`, `EPIX0074`, `EPIX0076`, `EPIX0127`, `EPIX0128`, `EPIX0129`, `EPIX0131`, `EPIX0134`, `EPIX0143`, `EPIX0009`, `EPIX0010`, `EPIX0041`, `EPIX0059`, `EPIX0008`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0017`, `EPIX0042`, `EPIX0018`, `EPIX0060`, `EPIX0075`, `EPIX0073`, `EPIX0030`, `EPIX0058`; events none listed.
- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /pix/v2/pix/out/scheduler`** (`post-schedule-pix-payment`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `scheduler_details`; response statuses 201, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples none; events `instantpay-scheduler-scheduler-status-change-1`, `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`PATCH /inst-pull-pay/v1/pix/automatic/{recurrence_id}`** (`update-recurrence-automatic`): security not declared; required parameters `Authorization` (header), `x-account` (header), `recurrence_id` (path); required body fields none declared; response statuses 204, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`PATCH /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}`** (`update-order-automatic-pix`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header), `x-account` (header), `end_to_end_id` (path); required body fields none declared; response statuses 204, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /inst-pull-pay/v1/pix/automatic/cancel`** (`cancel-recurrence-automatic`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `recurrence_id`, `reason_code`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /inst-pull-pay/v1/pix/automatic/payment/order/cancel`** (`cancel-automatic-pix-payment-order`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header), `x-account` (header); required body fields `end_to_end_id`, `reason`; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-schedule-pix-payment` | `instantpay-scheduler-scheduler-status-change-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-schedule-pix-payment` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-schedule-pix-payment` | `pix-pix-in-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |
| `post-schedule-pix-payment` | `pix-pix-out-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `pix-pix-out-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-out-1 | 3 | KU-EVT-catalogue-pix |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/pix-automatic.md`: updatedAt 2026-04-24T22:32:06.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 4 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/pix-automatic.md` | whole document | https://developers.pismo.io/pismo-docs/docs/pix-automatic | `6d7c5504f24242b8…` | 2026-04-24T22:32:06.000Z |

## Related knowledge units

- `KU-API-instant-payments-automatic-pix--automatic-pix` — API reference: Instant payments - Automatic Pix — Automatic Pix
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-qr-code--recurring-payment` — API reference: Instant payments - QR Code — Recurring payment
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
