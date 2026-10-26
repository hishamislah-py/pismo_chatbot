---
ku_id: KU-CARD-visa-colloboration-questionaire-part-06
title: Visa collaboration and allocation questionnaires (part 6 of 7)
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

# Visa collaboration and allocation questionnaires (part 6 of 7)

**KU ID:** `KU-CARD-visa-colloboration-questionaire-part-06` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/visa-colloboration-questionaire.md`:

> Valid if

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/visa-colloboration-questionaire.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/visa-colloboration-questionaire.md` lines 4444–5280 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire · updatedAt: 2026-10-05T16:49:10.000Z

<!-- source:begin path=docs/card-issuing/visa-colloboration-questionaire.md part=4443-5280 -->
  						<br/><br/>
  						<strong>Required</strong> when valid.
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CardholderReturnMerchandiseInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
  						<br/>
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CardholderAttemptReturnMerchandise</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left"></td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">howChAttemptReturnAndDispOfMerchandise</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Provide a detailed description of how the cardholder attempted to return merchandise
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and  
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CardholderAttemptReturnMerchandise</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">M</code> (Misrepresentation) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Merchandise</code> and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptReturnMerchandise</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  Values:
  						<br/>
  						<br/>

  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MRRM</code> = Merchant refused to accept returned merchandise
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MICNRM</code> = Merchant informed cardholder not to return the merchandise
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left; background-color:beige" colspan=4>
  						<strong>
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  							<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code>(Not as Described) 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described).
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseServiceReceivedDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date merchandise or service was received. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described)
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and DateDiff(
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseServiceReceivedDate</code>, Today())&gt;120 and DateDiff( Disputed Transaction&#x27;s Processing Date, Today())&gt;120
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
  					<td style="text-align:left">When did the negotiations begin? Format = CCYY-MM-DD
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
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
  					<td style="text-align:left">Explain the previous ongoing negotiations between the cardholder and merchant
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderMerchantPreviousNegotiationEvidence</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left"></td>
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">orderDetailsNotAsDescribed</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Provide details of what was ordered and not as described
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described)
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described)
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptToResolve</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
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
  					<td style="text-align:left">Did the cardholder return the merchandise. Y or N.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">'Merchandise'</code>.
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code> = 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  Values:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FF</code> = Face to Face
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FE</code> = Fed Ex
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code> = DHL
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">U</code> = UPS
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code> = Postal Service
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code> = Other
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">returnMethod</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">FE</code>(FedEx) OR 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">D</code>(DHL) OR 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">U</code> (UPS) OR 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">P</code>(Postal Service)) OR
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code>(Other)).
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReturnMerchandiseInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>.
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptReturnMerchandise</code> = 
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
  					<td style="text-align:left">Provide a detailed description of how the cardholder attempted to return merchandise
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptReturnMerchandise</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
  						<br/><b/>
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Merchandise</code> and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptReturnMerchandise</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>
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
  						<code>MNLER</code> = Merchant no longer exists or is not responding
  						<br/>
  						<code>MNPCIR</code> = Merchant did not provide clear instruction on how to return

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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Services&#x27;</code>
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code> = 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code> = 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantAcceptCancellationInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Did the merchant accept the cancellation? 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Services</code> and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code> is less than or equal to 15 days prior to current date.
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">qualityOfFoodInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is dispute related to the quality of food received from eating places or restaurants? 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Services</code> and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MCC</code> is 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">5812</code>, 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">5813</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">5814</code>.
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationMethod	
  						</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Cancellation Reason
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancel</code> = 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">nonFiatCurrencyNotMatching</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Was non-fiat currency or purchase of non-fungible token(s) (NFT), the non-fiat currency or non-fungible token received by the cardholder did not match the description provided at the time of the transaction? <code>Y</code> or <code>N</code>.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">MerchandiseOrServices</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Services</code>.
  						<br/><br/>
  						<strong>Required</strong> when valid.
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
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">ND</code> (Not as Described) and
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CardholderAttemptReturnMerchandise</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>.
  						<br/><br/>
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
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Q</code>(Quality) 
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to= 'Q' (Quality). 
  						<br/><br/>
  						<strong>Required</strong> when valid.
  						<br/><br/>
  						 Values: <br/>
  						 <code>Merchandise</code><br/>
  						 <code>Services</code>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/visa-colloboration-questionaire.md`: updatedAt 2026-10-05T16:49:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/visa-colloboration-questionaire.md` | body lines 4444–5280 | https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire | `34d9a4fbe7890f83…` | 2026-10-05T16:49:10.000Z |

## Related knowledge units

- None.
