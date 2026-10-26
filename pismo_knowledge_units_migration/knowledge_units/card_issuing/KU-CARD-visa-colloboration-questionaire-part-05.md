---
ku_id: KU-CARD-visa-colloboration-questionaire-part-05
title: Visa collaboration and allocation questionnaires (part 5 of 7)
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/visa-colloboration-questionaire.md
  sha256: 34d9a4fbe7890f83255e19591e5bc77b969861e043eb3fc3612753a164e2e875
  url: https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire
  role: primary_guide
  updated_at: '2026-10-05T16:49:10.000Z'
operations: []
related_kus: []
grouping_rationale: single source page; split into parts because the page is very large
---

# Visa collaboration and allocation questionnaires (part 5 of 7)

**KU ID:** `KU-CARD-visa-colloboration-questionaire-part-05` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/visa-colloboration-questionaire.md`:

> Valid if

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/visa-colloboration-questionaire.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/visa-colloboration-questionaire.md` lines 3475–4443 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire · updatedAt: 2026-10-05T16:49:10.000Z

<!-- source:begin path=docs/card-issuing/visa-colloboration-questionaire.md part=3474-4443 -->
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseReceivedDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date merchandise was received. Format = CCYY-MM=DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise).
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is there evidence of previous ongoing negotiations between the cardholder and merchant? 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and DateDiff(
  						<!-- -->, Today())&gt;120 and DateDiff( Disputed Transaction&#x27;s Processing Date, Today())&gt;120
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">whenNegotiationsBegin</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">When did the negotiations begin? Format = CCYY-MM-DD.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code>=&#x27;Y&#x27;
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">explainPrevNegotiation</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Explain the previous ongoing negotiations between the cardholder and merchant. 
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/><br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderFirstNotifiedIssuerDisputeDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date the cardholder first notified the issuer of the dispute. Format = CCYY-MM-DD.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise).
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">attemptToResolveProhLocalLaw</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is attempt to resolve prohibited by local law or regulations? Valid values = Y or N.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptToResolve</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Did the cardholder return the merchandise? 
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise).
  						<br/><br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnedMerchandiseDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date cardholder returned the merchandise. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code>=&#x27;Y&#x27;.
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantReceivedReturnedMerchandiseDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date merchant received the returned merchandise. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>.
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">returnMethod</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Return Method
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  Domain Values:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FF</code>=Face to Face
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FE</code>=Fed Ex
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code>=DHL
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">U</code>=UPS
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code>= Postal Service
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code>=Other
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">shippingTrackingNumber</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Tracking Number
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">returnMethod</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FE</code>(FedEx) OR 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code>(DHL) OR 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">U</code>(UPS) OR 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code>(Postal Service)).
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">howMerchandiseReturned</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Explain how the merchandise was returned
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">returnMethod</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code> (Other)
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptReturnMerchandise</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Did the cardholder attempt to return the merchandise? 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code>=&#x27;N&#x27;.
  						<br/><br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">attemptedReturnDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date of attempted return. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptReturnMerchandise</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>.
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">howChAttemptReturnAndDispOfMerchandise</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Provide a detailed description of how the cardholder attempted to return merchandise.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptReturnMerchandise</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantRefuseAdvise</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Provide certification of one of the following
  						<br/>

  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and &lt; 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CardholderAttemptReturnMerchandise</code>&gt;= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  Values:
  						<br/>

  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MRRM</code> = Merchant refused to accept returned merchandise
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MICNRM</code> = Merchant informed cardholder not to return the merchandise
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MNLER</code> = Merchant no longer exists or is not responding
  					    <br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MNPCIR</code> = Merchant did not provide clear instruction on how to return
  					
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispositionOfMerchandise</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">What is the disposition of the merchandise?
  						<br/>
  			

  Valid if <DisputeDueTo>='DM' (Damaged or Defective Merchandise) and <CardholderAttemptReturnMerchandise>='Y'.

  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">DM</code> (Damaged or Defective Merchandise) and 
  						<code>CardholderAttemptReturnMerchandise</code> = <code>Y</code>
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
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code>(Misrepresentation) 
  						</strong>
  					</td>

  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">What was purchased?
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) 
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseReceivedDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date merchandise was received. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Merchandise</code>.
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">serviceReceivedDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date services were received. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> =
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Services</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left"> Is there evidence of previous ongoing negotiations between the cardholder and merchant? 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Q</code> (Quality) and DateDiff(
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseReceivedDate</code> OR 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">serviceReceivedDate</code>, Today())&gt;120 and DateDiff( Disputed Transaction&#x27;s Processing Date, Today())&gt;120
  						<br/>
  						<br/>

  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">whenNegotiationsBegin</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">When did the negotiations begin?
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">explainPrevNegotiation</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Explain the previous ongoing negotiations between the cardholder and merchant
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M&#x27;</code>(Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderFirstNotifiedIssuerDisputeDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date the cardholder first notified the issuer of the dispute. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">whatWasPurchased</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Provide details of what was purchased
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation)
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">howMerchandiseOrServiceMisrepresented</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">How was the merchandise or service misrepresented?
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation)
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Did the cardholder cancel the services? 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Services</code>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Cancellation Date. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationMethod</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Cancellation Reason
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid.
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
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Merchandise</code>)
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">attemptToResolveProhLocalLaw</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is attempt to resolve prohibited by local law or regulations? 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptToResolve</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  						<strong>Note</strong>: If user inputs 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>, then application will display hard-stop error prompting the cardholder must attempt to resolve the dispute with the merchant unless it&#x27;s prohibited by local law or regulations.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Did the cardholder return the merchandise? 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Merchandise</code>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnedMerchandiseDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date cardholder returned the merchandise. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">returnedMerchandiseReceivedDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date cardholder returned the merchandise
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">returnMethod</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Return Method
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid
  						<br/>
  						<br/>
  Values:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FF</code>= Face to Face
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FE</code>= Fed Ex
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code>= DHL
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">U</code>= UPS
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code>= Postal Service
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code>= Other
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">howMerchandiseReturned</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Explain how the merchandise was returned
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">returnMethod</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code> (Other)
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">shippingTrackingNumber</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Tracking number
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) or <code>ReturnMethod</code>= 'FE'(FedEx) or 'D'(DHL) or 'U'(UPS) or 'P'(Postal Service) or 'O' (Other) 
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/visa-colloboration-questionaire.md`: updatedAt 2026-10-05T16:49:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/visa-colloboration-questionaire.md` | body lines 3475–4443 | https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire | `34d9a4fbe7890f83…` | 2026-10-05T16:49:10.000Z |

## Related knowledge units

- None.
