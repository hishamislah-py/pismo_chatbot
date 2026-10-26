---
ku_id: KU-EVT-client-webhooks-part-02
title: Client webhooks (part 2 of 14)
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/client-webhooks.md
  sha256: cd35b3bad1d1b22bcca9904923038c09b3581f0196a1afc2f4a7a436effd79f4
  url: https://developers.pismo.io/pismo-docs/docs/client-webhooks
  role: primary_guide
  updated_at: '2026-09-18T17:12:01.000Z'
operations: []
related_kus:
- KU-CARD-card-network-integration
grouping_rationale: single source page; split into parts because the page is very large
---

# Client webhooks (part 2 of 14)

**KU ID:** `KU-EVT-client-webhooks-part-02` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/client-webhooks.md`:

> limits

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/client-webhooks.md`: Client webhooks for card transaction authorization

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/client-webhooks.md` lines 838–1070 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/client-webhooks · updatedAt: 2026-09-18T17:12:01.000Z

<!-- source:begin path=docs/core-platform/client-webhooks.md part=837-1070 -->
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Account information.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 60px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>name</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Customer name</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 60px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>document_number</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Customer government document number.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 60px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>creation_date</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Creation datetime in ISO 8601 format.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 60px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>
                                                                                                                                                                                                                                                                                                                                                  								limits
                                                                                                                                                                                                                                                                                                                                                  							</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Limits</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 90px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>total</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>number</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Total</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 60px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>
                                                                                                                                                                                                                                                                                                                                                  								address
                                                                                                                                                                                                                                                                                                                                                  							</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Address information.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 90px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>zipcode</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Postal code</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 60px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>
                                                                                                                                                                                                                                                                                                                                                  								phone
                                                                                                                                                                                                                                                                                                                                                  							</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Phone information.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 90px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>area</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Area code.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 90px;">
                                                                                                                                                                                                                                                                                                                                                  							<code>country</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Country code.</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr>
                                                                                                                                                                                                                                                                                                                                                  						<td style="padding-left: 90px;"}>
                                                                                                                                                                                                                                                                                                                                                  							<code>number</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Phone number</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  					<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  						<td>
                                                                                                                                                                                                                                                                                                                                                  							<code>
                                                                                                                                                                                                                                                                                                                                                  								metadata
                                                                                                                                                                                                                                                                                                                                                  							</code>
                                                                                                                                                                                                                                                                                                                                                  						</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>Any JSON name-value pairs</td>
                                                                                                                                                                                                                                                                                                                                                  						<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  					</tr>
                                                                                                                                                                                                                                                                                                                                                  				</tr>
                                                                                                                                                                                                                                                                                                                                                  		<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  			<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>
                                                                                                                                                                                                                                                                                                                                                  					raw
                                                                                                                                                                                                                                                                                                                                                  				</code>
                                                                                                                                                                                                                                                                                                                                                  			</td>
                                                                                                                                                                                                                                                                                                                                                  			<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  			<td>Platform additional information forwarded to the anti-fraud system, varies  according to origin. Sent only in on-us transactions.</td>
                                                                                                                                                                                                                                                                                                                                                  			<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  		</tr>
                                                                                                                                                                                                                                                                                                                                                  			</table>
          `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample request</summary>

    ```json
    {
      "decision": "approve",
      "id": "id",
      "datetime": "2022-07-28T12:45:12.566Z",
      "account_id": 102334690,
      "currency_code": "986",
      "amount": 20,
      "origin": "banking",
      "operation_type": "cashin",
      "processing_code": "003100",
      "entities": {
        "account": {
          "name": "Anne Arbor",
          "document_number": "8675309",
          "creation_date": "2023-01-01T05:00:00.000Z",
          "limits": {
            "total": 1000
          },
          "address": {
            "zipcode": 8675309
          },
          "phone": {
            "area": "415",
            "country": "55",
            "number": "8675309"
          }
        }
      },
      "metadata": {
        "a": false,
        "b": 1,
        "c": "test",
        "d": {
          "d1": "4683bf0c-20d2-4a7f-8877-5f3e9b46252c",
          "d2": false,
          "d3": 15
        }
      }
    }
    ```
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}> Response fields</summary>

    <HTMLBlock>
      {`
                                                                                                                                                                                                                                                                                                                                                  <table>
                                                                                                                                                                                                                                                                                                                                                  	<tr style="background-color: lightgrey";>
                                                                                                                                                                                                                                                                                                                                                  		<th>Field</th>
                                                                                                                                                                                                                                                                                                                                                  		<th>Type</th>
                                                                                                                                                                                                                                                                                                                                                  		<th>Description</th>
                                                                                                                                                                                                                                                                                                                                                  		<th>Req</th>
                                                                                                                                                                                                                                                                                                                                                  	</tr>
                                                                                                                                                                                                                                                                                                                                                  	<tr>
                                                                                                                                                                                                                                                                                                                                                  		<td>
                                                                                                                                                                                                                                                                                                                                                  			<code>decision</code>
                                                                                                                                                                                                                                                                                                                                                  		</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>string</td>
                                                                                                                                                                                                                                                                                                                                                  		<td>Client decision
                                                                                                                                                                                                                                                                                                                                                  			<br>Enum: [ "
                                                                                                                                                                                                                                                                                                                                                  				<code>approve</code>", "
                                                                                                                                                                                                                                                                                                                                                  				<code>reject</code>"]
                                                                                                                                                                                                                                                                                                                                                  			</td>
                                                                                                                                                                                                                                                                                                                                                  			<td>Y</td>
                                                                                                                                                                                                                                                                                                                                                  		</tr>
                                                                                                                                                                                                                                                                                                                                                  		<tr style="background-color: beige;">
                                                                                                                                                                                                                                                                                                                                                  			<td>
                                                                                                                                                                                                                                                                                                                                                  				<code>
                                                                                                                                                                                                                                                                                                                                                  					metadata
                                                                                                                                                                                                                                                                                                                                                  				</code>
                                                                                                                                                                                                                                                                                                                                                  			</td>
                                                                                                                                                                                                                                                                                                                                                  			<td>object</td>
                                                                                                                                                                                                                                                                                                                                                  			<td>Any JSON name-value pairs</td>
                                                                                                                                                                                                                                                                                                                                                  			<td>N</td>
                                                                                                                                                                                                                                                                                                                                                  		</tr>

                                                                                                                                                                                                                                                                                                                                                  	</table>
          `}
    </HTMLBlock>
  </details>

  <details>
    <summary style={{fontSize: "medium", fontWeight: "bold"}}>Sample response </summary>

    ```json
    {
        “decision”: “approve”,
        “metadata”: {}
     }
    ```
  </details>
</details>

# Client webhooks for card transaction authorization

The following webhooks are called, if clients have registered them with Pismo, during the card transaction authorization process. They allow clients to do their own validation and anti-fraud checks in addition to those that Pismo does.

> 🚧 Different webhooks for Full balance and Zero balance
>
> Please note that the following two webhooks - one for Full balance clients and one for Zero balance clients - are **not** the same and can **not** be used interchangeably.

For information about the differences between Full balance and Zero balance implementation, refer to the [Card network integration](https://developers.pismo.io/pismo-docs/docs/card-network-integration) guide.
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/client-webhooks.md`: updatedAt 2026-09-18T17:12:01.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/client-webhooks.md` | body lines 838–1070 | https://developers.pismo.io/pismo-docs/docs/client-webhooks | `cd35b3bad1d1b22b…` | 2026-09-18T17:12:01.000Z |

## Related knowledge units

- `KU-CARD-card-network-integration` — Card network integration and certification
