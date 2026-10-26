---
ku_id: KU-CARD-visa-colloboration-questionaire-part-02
title: Visa collaboration and allocation questionnaires (part 2 of 7)
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

# Visa collaboration and allocation questionnaires (part 2 of 7)

**KU ID:** `KU-CARD-visa-colloboration-questionaire-part-02` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/visa-colloboration-questionaire.md`:

> Valid if

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/visa-colloboration-questionaire.md`: no headings

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/visa-colloboration-questionaire.md` lines 934–1588 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire · updatedAt: 2026-10-05T16:49:10.000Z

<!-- source:begin path=docs/card-issuing/visa-colloboration-questionaire.md part=933-1588 -->
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderDeceased</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Certification that the cardholder is deceased
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction) and disputed transaction&#x27;s jurisdiction is Europe regional or domestic within Europe
  						<br/>
  						<br/>
  						<strong>Note</strong>: User can only provide either 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantFacilitiesWithdrawn</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderDeceased</code> not both. If both fields are provided then application will display hard stop error.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Cancellation Date / Date cardholder withdrew permission to charge the Payment Credential. Format = CCYY-MM-DD
  						<br/>
  						<br/>
  For Europe regional or domestic within Europe:
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction) and (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantFacilitiesWithdrawn</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">false</code> AND 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderDeceased</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">false</code>)
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  For all other jurisdiction other than Europe regional or domestic:
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction)
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  						<strong>Note</strong>: User can only provide either 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">accountClosureDate</code> for all jurisdictions.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodWithMerchantInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Contact method with merchant
  						<br/>
  						<br/>
  For other jurisdiction other than Europe regional or domestic:
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code> is not null.
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">EmailValid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodWithMerchantInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>When valid, at least one of the following fields must be set to 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantMailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantInPersonInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Call Center Phone Number
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodWithMerchantInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  When valid, at least one of the following fields must be set to 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>: 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantMailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantInPersonInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantMailInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Mail
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodWithMerchantInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  When valid, at least one of the following fields must be set to 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantMailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantInPersonInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">SMS/Text Message
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodWithMerchantInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  When valid, at least one of the following fields must be set to 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantMailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantInPersonInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantInPersonInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">In-Person
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodWithMerchantInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  When valid, at least one of the following fields must be set to 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantMailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantInPersonInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Webform/Application Name
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodWithMerchantInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  When valid, at least one of the following fields must be set to 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>: 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantMailInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantInPersonInd</code>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code>
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMerchantDetailsPhoneNumber</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Phone Number
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantCallCenterInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantSMSInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMerchantDetailsEmailAddress</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Email Address
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantEmailInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMerchantDetailsPhysicalAddress</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Physical Address
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code> =
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code> or 
  						<code>contactMethodMerchantInPersonInd</code> = <code>true</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMerchantDetailsApplicationName</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Application Name
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">contactMethodMerchantWebformInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">otherFormOfPaymentInd</code>
  					</td>
  					<td style="text-align:left">bool</td>
  					<td style="text-align:left">Other Form of Payment
  						<br/>
  						<br/>
  For other jurisdiction other than Europe regional or domestic:
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code> is not 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">null</code>.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">otherFormOfPaymentDesc</code>
  					</td>
  					<td style="text-align:left">string </td>
  					<td style="text-align:left">Describe other form of payment
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">otherFormOfPaymentInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">accountClosureDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">Date issuer informed merchant of account closure
  						<br/>
  						<br/>
  For Europe regional or domestic within Europe:
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction) and (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">merchantFacilitiesWithdrawn</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">false</code> AND 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderDeceased</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">false</code>)
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  For all other jurisdiction other than Europe regional or domestic:
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction)
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid.
  						<br/>
  						<br/>
  						<strong>Note</strong>: User can only provide either CancellationDate or AccountClosureDate for all jurisdictions.
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
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CR</code> (Cancelled Recurring Transaction) and user supplied value in 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code>
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
  							<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CS</code>(Cancelled Merchandise/Service) 
  						</strong>
  					</td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">attemptToResolveProhLocalLaw</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Is attempt to resolve prohibited by local law or regulations? Valid values =<br/> 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code><br/><br/>Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code>=
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CS</code>(Cancelled Merchandies/Services) and 
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderAttemptToResolve</code>= 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code><br/><br/>
  						<strong>Required</strong> when valid.<br/>
  						<strong>Note</strong>: If user inputs 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>, then application will display hard-stop error prompting the cardholder must attempt to resolve the dispute with the merchant unless it’s prohibited by local law or regulations.

  					</td>
  					<td style="text-align:left"></td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationPolicyProvidedInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Was a cancellation policy provided? 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code> or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>
  						<br/>
  						<br/>
  						<strong>Required</strong> if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CS</code> (Cancelled Merchandise/Services) and any of the following is 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">true</code>:
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cardholderReceiveMerchandiseInd</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>; or
  						<br/>
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancelBeforeShipping</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Y</code>; or
  						<br/>
  (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">serviceType</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">G</code> (Guaranteed Reservation); or
  						<br/>
  (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">serviceType</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">T</code> (Timeshare) and 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code> is 14 days greater than 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">timeshareDate</code>)
  						<br/>
  						<br/>
  						<strong>Optional</strong> if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CS</code> (Cancelled Merchandise/Services) and (
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">serviceType</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">O</code> (Other) or 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">didCardholderCancelBeforeShipping</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">N</code>)
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
  				<tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">disputeRelateToOffpremisesDistanceSellInd</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">Does the dispute relate to off-premises or distance selling contract? Valid values = Y or N.
  						<br/>
  						<br/>
  Valid if 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dispute_due_to</code> = 
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">CS</code> (Cancelled Merchandise/Services) and jurisdiction is Europe regional or domestic within Europe for non T&amp;E transactions and merchant is located in country other than Turkey, Switzerland and Israel.
  						<br/>
  						<br/>
  						<strong>Required</strong> when valid
  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationDate</code>
  					</td>
  					<td style="text-align:left">date</td>
  					<td style="text-align:left">

                          Cancellation Date.<br/><br/>
                           

  						<strong>Required</strong> if <code>dispute_due_to</code> =<code>'CS'</code> (Cancelled Merchandise/Services) and <code>MerchandiseOrServices </code>=<code>'Services'</code> and <code>DidCardholderCancel</code>=<code>'Y'</code> or <code>CertificationGuaranteedReservation</code>=<code>'GR'</code> (The cardholder properly cancelled the guaranteed reservation) or <code>CertificationGuaranteedReservation</code>=<code>'RC'</code> (The cardholder attempted to cancel within 24 hours of delivery of the reservation confirmation) or <code>MerchandiseOrServices</code>=<code>'Merchandise'</code> and <code>DidCardholderCancelBeforeShipping</code> = <code>'Y'</code> or <code>MerchandiseOrServices</code>=<code>'Merchandise'</code> and <code>DidCardholderCancel</code>=<code>'Y'</code> and <code>CardholderReceiveMerchandiseInd</code>=<code>'N'</code>
  						<br/>
  						<br/>
  						Optional if <code>DisputeDueTo</code>=<code>'CS'</code> (Cancelled Merchandise/Services) and <code>MerchandiseOrServices</code>=<code>'Merchandise'</code> and <code>DidCardholderCancelBeforeShipping</code>=<code>'N'</code>

  					</td>
  					<td style="text-align:left">C</td>
  				</tr>
                  <tr>
  					<td style="text-align:left">
  						<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>
  						<code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">cancellationMethod</code>
  					</td>
  					<td style="text-align:left">string</td>
  					<td style="text-align:left">

                          Cancellation Method
                          <br/>
  						<br/>
  						<strong>Required</strong> if <code>DisputeDueTo</code>=<code>'CS'</code> (Cancelled Merchandise/Services) and (<code>MerchandiseOrServices </code>=<code>'Services'</code> and <code>DidCardholderCancel</code>=<code>'Y'</code>) or (<code>MerchandiseOrServices</code>=<code>'Merchandise'</code> and <code>DidCardholderCancel</code>=<code>'Y'</code> and <code>CardholderReceiveMerchandiseInd</code>=<code>'N'</code>) or (<code>MerchandiseOrServices</code>=<code>'Merchandise'</code> and <code>DidCardholderCancelBeforeShipping</code>=<code>'Y'</code>)
                          <br/> 
  						<br/>
  						Optional if <code>DisputeDueTo</code>=<code>'CS'</code> (Cancelled Merchandise/Services) and <code>DidCardholderCancelBeforeShipping</code>=<code>'N'</code>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/visa-colloboration-questionaire.md`: updatedAt 2026-10-05T16:49:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/visa-colloboration-questionaire.md` | body lines 934–1588 | https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire | `34d9a4fbe7890f83…` | 2026-10-05T16:49:10.000Z |

## Related knowledge units

- None.
