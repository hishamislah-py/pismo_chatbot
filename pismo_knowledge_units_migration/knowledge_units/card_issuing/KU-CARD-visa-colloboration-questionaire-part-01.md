---
ku_id: KU-CARD-visa-colloboration-questionaire-part-01
title: Visa collaboration and allocation questionnaires (part 1 of 7)
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/visa-colloboration-questionaire.md
  sha256: 34d9a4fbe7890f83255e19591e5bc77b969861e043eb3fc3612753a164e2e875
  url: https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire
  role: primary_guide
  updated_at: '2026-10-05T16:49:10.000Z'
operations:
- post-v1-disputes-disputeId-forms
- post-v1-networkauthorization-disputes
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--supporting-forms
- KU-EVT-catalogue-disputes
grouping_rationale: single source page; split into parts because the page is very large
---

# Visa collaboration and allocation questionnaires (part 1 of 7)

**KU ID:** `KU-CARD-visa-colloboration-questionaire-part-01` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/visa-colloboration-questionaire.md`:

> This guide is intended to help clients [create a dispute form](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-forms)  for Visa. Creating this form follows [creating a dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes).  Specifically, it is   a transcription from Visa IES Release 23.2 translated to the Pismo platform processing.  It is intended to help the clients use the Visa Dispute form collaboration questionnaire. For more information, see  the Visa IES Release 23.2 spreadsheet or contact your Pismo representative.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/visa-colloboration-questionaire.md`: Visa collaboration and allocation questionnaires; Processing errors (reason 12); Consumer disputes (reason 13)

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/visa-colloboration-questionaire.md` lines 1–933 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire · updatedAt: 2026-10-05T16:49:10.000Z

<!-- source:begin path=docs/card-issuing/visa-colloboration-questionaire.md part=0-933 -->

# Visa collaboration and allocation questionnaires

This guide is intended to help clients [create a dispute form](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-forms)  for Visa. Creating this form follows [creating a dispute](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes).  Specifically, it is   a transcription from Visa IES Release 23.2 translated to the Pismo platform processing.  It is intended to help the clients use the Visa Dispute form collaboration questionnaire. For more information, see  the Visa IES Release 23.2 spreadsheet or contact your Pismo representative.

This document addresses two dispute reasons:

* Processing Errors (reason 12)
* Consumer (reason 13).

So if your dispute has a reason 12,  see the **Result of processing errors (Reason 12)** section below.

For more information, see <a href="https://www.chargebackgurus.com/chargeback-reason-codes" target="_blank">Visa chargeback reason codes</a>. Specifically, Processing errors (reason 12), and Consumer Disputes (reason 13).

Inside the result sections you can see that some fields are repeated. This occurs because the same field could be used for more than one `dispute_due_to` value. The tables below are organized according to `dispute_due_to` values.

Pismo does not validate the completed collaboration questionnaire content.

# Processing errors (reason 12)

**Note**: For the **Req** column, `C` = Conditional, `Y` = required, `N`= not required, and `N/A` = not applicable

<HTMLBlock>
  {`
  <button class="modal-button" href="#htmlTable2">View table<i class="icon-maximize2"onclick="event.target.parentElement.click()"></i></button>
  <dialog class="modal" id="htmlTable2">
  <form class="form" method="dialog">
  <div class="modal-header">  
  <h2>Result of processing errors (reason 12)</h2>
  <span class="close">&times;</span>
  </div>
  <div class="table-wrapper">
  		<table>
  			<thead>
  				<tr>
  					<th style="text-align:left">Field</th>
  					<th style="text-align:left">Type</th>
  					<th style="text-align:left">Description</th>
  					<th style="text-align:left">Req</th>
  				</tr>
  			</thead>
  			<tbody>

  				<tr id="ID">
  					<td style="text-align:left; background-color: beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ID</code> (Invalid Data)
  						</strong>
  					</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">authorizationRequestDeclinedValidDataInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Certification that the authorization request would have been declined if valid data had been provided.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ID</code> (Invalid Data).<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">explainWhyValidDataInclusionReason</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Explain why the inclusion of valid data would have caused the Authorization Request to be declined
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ID</code> (Invalid Data).  
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left; background-color:beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">LP</code> (Late Presentment)
  						</strong>
  					</td>
  				</tr>

                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">processingDateOver10DaysFmTransDateInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Processing Date is more than 10 days from  the Transaction Date. Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> =
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">LP</code> (Late Presentment). and if application determines that Processing Date > 10 calendar days from Transaction Date.
  						<br/>
  						<br/>
                          This element is valid only for Interlink network.
                          For Non interlink network including adjustment of an ATM cash disbursement or a PIN-Authenticated Visa Debit Transaction: Required if Processing Date &lt;= 180 calendar days from Transaction Date for non adjustment transaction or if Processing Date &lt;= 45 calendar days from Transaction Date for adjustment transaction.
  						<br/>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">processingDateOver45DaysFmTransDateInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Processing Date is more than 45 days from the Transaction Date.<br/>For non-interlink network:<br/> Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> =
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">LP</code> (Late Presentment) and if Processing Date for an adjustment of ATM Cash Disbursement/PAVD transaction > 45 calendar days from Transaction Date.
  						<br/>
                          For Interlink network:<br/> Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> =
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">LP</code> (Late Presentment) and Processing Date of an adjustment transaction > 45 calendar days from Transaction Date.
  						
  						<br/>
     
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>

                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">processingDateOver180DaysFmTransDateInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Processing Date is more than 180 days from the Transaction Date. Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> =
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">LP</code> (Late Presentment) and if application determines that Processing Date > 180 calendar days from Transaction Date.
  						<br/>
  						<br/>
                          This element is valid only for Interlink network.
     
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left; background-color: beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IC</code> (Incorrect Currency)
  						</strong>
  					</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">incorrectCurrencyReason</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Incorrect currency reason.
  						<br/>
  Valid in VISA Processing Errors Flux (reason code 12.3).
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CD</code> = Currency different. The transaction currency is different from the currency transmitted through Visa.
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DD</code> = Cardholder claims that you failed to offer them a choice of paying in your local currency or that they declined paying in their local currency
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">correctCurrency</code>
  					</td>
  					<td style="text-align:left">number</td>
  					<td style="text-align:left">Processed through VisaNet as [currency code]; what was the correct currency
  						<br/>
  [followed by unlabeled alpha currency code dropdown]
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IC</code> (Incorrect Currency) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">incorrectCurrencyReason</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CD</code> (Currency Difference)
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid
  						<br/>
  						<br/>
  						<strong>Note</strong>: Provide correct 3-digit ISO currency code as opposed to the one in the original transaction being disputed.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderDidNotAgreeDCC</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Certification that the Cardholder did not agree to Dynamic Currency Conversion and did not make an active choice.
  						<br/>
  Valid values = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IC</code> (Incorrect Currency) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">incorrectCurrencyReason</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DD</code> (DCC Dispute)
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left; background-color:beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IT</code> (Incorrect Transaction Code)
  						</strong>
  					</td>

  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">transactionCodeIncorrect</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">How is transaction code incorrect?
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IT</code> (Incorrect Transaction Code).
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  Values:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CRI</code>= Credit instead of reversal or adjustment,
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CRD</code>= Credit posted as a debit,
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DCR</code>= Debit posted as a credit
  						<br/>
  						<br/>
  Retired values:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CP</code>= Cash posted as purchase,
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">PC</code>= Purchase posted as cash.
  						<br/>
  						<br/>
  						<strong>Notes</strong>:
  						<br/>
  						<br/>
  1. If user selects 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CRI</code> (Credit instead of reversal or adjustment) then the dispute amount must always be a partial amount else user will get a hard stop error upon submit if Dispute Amount &gt;= Transaction Amount.
  						<br/>
  						<br/>
  2. If user selects 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CRD</code> (Credit posted as a debit) or &#x27;DCR&#x27; (Debit posted as a credit) then the Dispute Amount should be twice the Transaction Amount.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">rolTransactionId</code>
  					</td>
  					<td style="text-align:left">long</td>
  					<td style="text-align:left">Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IT</code> (Incorrect Transaction Code) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">transactionCodeIncorrect</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CRI</code> (Credit instead of reversal or adjustment)
  						<br/>
  						<br/>
  This will be VROL internal transaction id. User must provide one of the two fields 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">rolTransactionId</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">incorrectTransactionId</code>. These fields will be used to initiate transaction inquiry to search for supporting transaction. If provided, this field will take precedence over 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">incorrectTransactionId</code>.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">incorrectTransactionId</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IT</code> (Incorrect Transaction Code) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">transactionCodeIncorrect</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CRI</code> (Credit instead of reversal or adjustment)
  						<br/>
  						<br/>
  User must provide one of the two fields incorrectTransactionId or rolTransactionId.
  						<br/>
  						<br/>
  These fields will be used to initiate transaction inquiry to search for supporting transaction.
  						<br/>
  						<br/>
  This is VisaNet transaction id. The Transaction ID is specified as the first 15 digits of this field from original transaction. If a Multiple Clearing Sequence Number (MCSN) is present for transactions such as airline transactions,
  						<br/>
  the MCSN should be appended to the end of the Transaction ID, which would make this a 17 digit value. A blank MCSN is treated the same as two zeros at the end of the Transaction ID.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">explainWhyCreditRefund ProcessedInError</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Explain why the credit refund was processed in error
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IT</code> (Incorrect Transaction Code) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">transactionCodeIncorrect</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CRI</code> (Credit instead of reversal or adjustment).
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  The dispute amount will be a partial amount.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>

  				<tr>
  					<td style="text-align:left; background-color:beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IAN</code> (Incorrect Account Number)
  						</strong>
  					</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">receiptAccountNumberMatchInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">
  						Does the account number on the receipt match the cardholder's account number or token? Valid values = Y or N.<br/>
  	
  						<br/<br/>Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IT</code> (Incorrect Account Number) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IssuerMasterFileAccountNumberInd</code>= 'Y'
  						<br/>
  						<strong>Required</strong> when valid.

  					</td>
  					<td style="text-align:left"></td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">issuerMasterFileAccountNumberInd</code>
  					</td>
  					<td style="text-align:left">long</td>
  					<td style="text-align:left">Is the account number on the issuer&#x27;s master file? Valid values = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IAN</code> (Incorrect Account Number)
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">matchingAuthTranId</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">
                          Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IAN</code> (Incorrect Account Number) and <code>IssuerMasterFileAccountNumberInd</code>=\`N\` and if a matching authorization transaction exists
  						<br/>
  						This is VROL internal transaction id
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">authorizationDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">
                          Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IAN</code> (Incorrect Account Number) and <code>IssuerMasterFileAccountNumberInd</code>=\`N\` and if a matching authorization transaction exists
  						<br/>
  						This is VROL internal transaction id
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">authorizationCode</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">
                          Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IAN</code> (Incorrect Account Number) and <code>IssuerMasterFileAccountNumberInd</code>=\`N\` and if a matching authorization transaction exists
  						<br/>
  						This is VROL internal transaction id
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left; background-color:beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IA</code> (Incorrect Amount)
  						</strong>
  					</td>

  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReceiptAmt</code>
  					</td>
  					<td style="text-align:left">number</td>
  					<td style="text-align:left">What is the amount on the cardholder&#x27;s receipt. Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IA</code> (Incorrect Amount). 
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  						<strong>Note</strong>: VROL calculates the difference between the transaction amount and the amount on the cardholder&#x27;s receipt. If the dispute amount is more than the difference, VROL displays a hard-stop error and expect the user to modify the dispute amount to be no more than the difference.
  						<br/>
  						<br/>
  						<strong>Note</strong>: Documentation is 
  						<strong>required</strong>.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantDisputePriceDiffInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is the dispute due to the difference between the quoted price and the actual charges made by the merchant?
  						<br/>
  						<br/>Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">IA</code>(Incorrect Amount) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReceiptAmt</code> not equal to 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">TransactionAmount</code> and must be a valid T&amp;E MCC code transaction as listed in the Visa Op Regs.
  						<br/>
  						<br/>
  						Valid values = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left; background-color:beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code> (Duplicate) or 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other means)
  						</strong>
  					</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">bothTransactionsOnSameAcctNumberInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Are both transactions for the same merchant and on the same card? Valid values = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code> (Duplicate) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means).
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>


                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">duplicateARN</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">
                          Acquirer Reference Number
  						<br/>
                          Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code> (Duplicate) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means).
                          and <code>bothTransactionsOnSameAcctNumberInd</code>= <code>Y</code>.
  						<br/>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>


  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">issuerOrCardholderOtherAcctWithDiffVisaCardInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is the other transaction for the same merchant and on a different Visa Card owned by the same Issuer/Cardholder?
  						<br/>
  						Format= CYY-MM-DD
  						<br/><br/>

  Valid if (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code> (Duplicate) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means)) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">bothTransactionsOnSameAcctNumberInd</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">issuerEvidenceMerchantPassedOnFundsInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Does the issuer have evidence that the first merchant passed on the funds to the second merchant? Valid values = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  Valid if (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code> (Duplicate) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means)) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">providingPaymentProofOtherMeans</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">V</code> (Voucher from the third party))
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  						<strong>Note</strong>: If user inputs 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>, then the attachments docs are required. If user inputs 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>, then dispute will be blocked with a hard stop error.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptToResolve</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Did the cardholder attempt to resolve the dispute with the merchant?
  						<br/>
  						<br/>
  						<strong>Required</strong> if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means) AND (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">otherTranSameMerchantInd</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">issuerOrCardholderOtherAcctWithDiffVisaCardInd</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>)
  						<br/>
  						Valid values = Y or N.
  						<br/>
  Optional if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code> (Duplicate) AND (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">otherTranSameMerchantInd</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">issuerOrCardholderOtherAcctWithDiffVisaCardInd</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>)
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">attemptToResolveProhLocalLaw</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is attempt to resolve prohibited by local law or regulations? Valid values = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code>(Duplicate) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptToResolve</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">1N</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  						<strong>Note</strong>: If user inputs 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>, then application will display hard-stop error prompting the cardholder must attempt to resolve the dispute with the merchant unless it’s prohibited by local law or regulations.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">otherTranSameMerchantInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is the other transaction paid by other means? Valid values = Y or N.
  						<br/>
  						<br/>
                          <b>Note</b>: If user inputs 'N', then dispute will be blocked with a hard stop error.
                          <br/>
  						<br/>
  Valid if (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code>(Duplicate) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means)) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">issuerOrCardholderOtherAcctWithDiffVisaCardInd</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
  						<br/>
                          
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">providingPaymentProofOtherMeans</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Providing proof of payment by other means
  						<br/>
  						<br/>
  Valid if (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code>(Duplicate) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> (Paid by other Means)) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">otherTranSameMerchantInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>.
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  Domain Values:
  						<br/>
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">A</code>= ARN from other transaction if paid with Visa Card
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">T</code>= Transaction information from other transaction (Transaction Identifier), if paid with Visa card
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">C</code>= Cash Receipt
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">F</code>= Copy of the front and back of a cancelled check
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">V</code>= Voucher from the third party
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">S</code>= Statement from other card
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code>= Other
  						<br/>
  						<br/>
  Documentation is required and valid for domain values 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">C</code>, 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">F</code>, 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">S</code> and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code>.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>


  			</tbody>
  		</table>
  	</div>
  `}
</HTMLBlock>

# Consumer disputes (reason 13)

**Note**: For the **Req** column, `C` = Conditional, `Y` = required, `N`= not required, `N/A` = not applicable, and `VROL` = <a href="https://usa.visa.com/solutions/post-purchase-solutions/visa-resolve-online.html" target="_blank">Visa Resolve On Line</a>

<HTMLBlock>
  {`
  <button class="modal-button" href="#htmlTable3">View table<i class="icon-maximize2"onclick="event.target.parentElement.click()"></i></button>
  <dialog class="modal" id="htmlTable3">
  <form class="form" method="dialog">
  <div class="modal-header">  
  <h2>Result of consumer disputes (reason 13)</h2>
  <span class="close">&times;</span>
  </div>
  <div class="table-wrapper">
  		<table>
  			<thead>
  				<tr>
  					<th style="text-align:left">Field</th>
  					<th style="text-align:left">Type</th>
  					<th style="text-align:left">Description</th>
  					<th style="text-align:left">Req</th>
  				</tr>
  			</thead>
  			<tbody>
  				<tr>
  					<td style="text-align:left; background-color:beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code>(Cancelled Recurring Transaction) 
  						</strong>
  					</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantFacilitiesWithdrawn</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Certification that the merchant facilities were withdrawnValid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction) and disputed transaction&#x27;s jurisdiction is Europe regional or domestic within Europe
  						<strong>Note</strong>: User can only provide either merchantFacilitiesWithdrawn or cardholderDeceased not both. If both fields are provided then application will display hard stop error.
  					</td>
  					<td style="text-align:left"></td>
  				</tr>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/disputes/{disputeId}/forms` | `post-v1-disputes-disputeId-forms` | Create dispute form | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | Create dispute | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01 |

### Operation essentials

- **`POST /v1/disputes/{disputeId}/forms`** (`post-v1-disputes-disputeId-forms`): security `BearerAuth`; required parameters `disputeId` (path); required body fields `form`; response statuses 200, 401, 404, 422, 500; error codes in examples none; events none listed.
- **`POST /v1/networkauthorization-disputes`** (`post-v1-networkauthorization-disputes`): security `BearerAuth`; required parameters `Authorization` (header); required body fields `modality`, `disputed_amount`, `is_partial`, `network_brand_type`; response statuses 200, 400, 401, 422, 500; error codes in examples none; events `disputes-dispute-installment-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-networkauthorization-disputes` | `disputes-dispute-installment-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/visa-colloboration-questionaire.md`: updatedAt 2026-10-05T16:49:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/visa-colloboration-questionaire.md` | body lines 1–933 | https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire | `34d9a4fbe7890f83…` | 2026-10-05T16:49:10.000Z |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--supporting-forms` — API reference: Card issuing - Disputes — Supporting forms
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
