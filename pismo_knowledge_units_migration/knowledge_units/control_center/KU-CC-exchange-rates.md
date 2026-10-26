---
ku_id: KU-CC-exchange-rates
title: Exchange rates in Control Center
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/exchange-rates.md
  sha256: a00b028f199e0a21e29b5e2722021560ffa253929b88ae974007bca144667f22
  url: https://developers.pismo.io/pismo-docs/docs/exchange-rates
  role: primary_guide
  updated_at: '2026-05-29T15:23:03.000Z'
operations:
- createExchangeRates
related_kus:
- KU-API-platform-setup-rates-and-fees--exchange-rates
- KU-CORE-exchange-rate
grouping_rationale: single source page
---

# Exchange rates in Control Center

**KU ID:** `KU-CC-exchange-rates` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/exchange-rates.md`:

> The Pismo platform supports multi-currency exchange rates for international transactions. By default, daily exchange rates are defined at the organization level.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/exchange-rates.md`: Exchange rates in Control Center; View exchange rates; Create an exchange rate; Bulk upload exchange rates

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/exchange-rates.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/exchange-rates · updatedAt: 2026-05-29T15:23:03.000Z

<!-- source:begin path=docs/control-center/exchange-rates.md part=0-end -->

# Exchange rates in Control Center

The Pismo platform supports multi-currency exchange rates for international transactions. By default, daily exchange rates are defined at the organization level.

> 📘 Exchange rates for international transactions
>
> If you have network acceptance for international purchases, the last rate configured less than or equal to the rate date is used. If no exchange rate is created, an error is returned. Refer to [Exchange rates for international transactions](https://developers.pismo.io/pismo-docs/docs/exchange-rate#exchange-rates-for-international-transactions)  for more information.

For more information on exchange rates, refer to the following:

* [Exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rate)
* [Exchange rates API](https://developers.pismo.io/pismo-docs/reference/createexchangerates)

From Control Center, you can:

* [View exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rates#view-exchange-rates)
* [Create an exchange rate](https://developers.pismo.io/pismo-docs/docs/exchange-rates#create-an-exchange-rate)
* [Bulk upload exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rates#bulk-upload-exchange-rates)

# View exchange rates

To view exchange rates:

1. From the main menu, select **Configurations** > **Exchange rates**.
2. On the **Exchange rates** screen,  you can view organizations and programs and their daily exchange rates. The table shown includes the following fields.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        API Parameters
      </th>

      <th>
        Type
      </th>

      <th>
        Validation Rules
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Program ID or ORG
      </td>

      <td>
        The program or organization this exchange rate is associated with.
      </td>

      <td>
        `program_id` OR the word "ORG"
      </td>

      <td>
        number
      </td>

      <td>
        For programs, the program ID\
        For orgs only, the word ""ORG""
      </td>
    </tr>

    <tr>
      <td>
        Origin currency code
      </td>

      <td>
        The three-letter ISO 4217 code representing the currency from which the exchange is being calculated. The code must be listed in Control Center.
      </td>

      <td>
        `origin_currency_id`
      </td>

      <td>
        string
      </td>

      <td>
        Control Center list of three-letter ISO 4217 currency codes
      </td>
    </tr>

    <tr>
      <td>
        Destination currency code
      </td>

      <td>
        The three-letter ISO 4217 code representing the currency you are converting into. The code must be listed in Control Center.
      </td>

      <td>
        `destination_currency_id`
      </td>

      <td>
        string
      </td>

      <td>
        Control Center list of three-letter ISO 4217 currency codes
      </td>
    </tr>

    <tr>
      <td>
        Exchange rate
      </td>

      <td>
        The wholesale exchange rate amount in the destination currency. The wholesale exchange rate is the real market rate without any added fees. You can enter up to 4 decimal places.
      </td>

      <td>
        `exchange_rate`
      </td>

      <td>
        number
      </td>

      <td>
        Number up to 4 decimal points
      </td>
    </tr>

    <tr>
      <td>
        Spread
      </td>

      <td>
        The percentage markup added to the base exchange rate to account for conversion costs or profit. You can enter up to 4 decimal places.

        For example: a spread value of 1.1205 means a 1.1205% markup is added to the exchange rate. This is the percentage the issuer charges for converting currency on that day."
      </td>

      <td>
        `spread`
      </td>

      <td>
        number
      </td>

      <td>
        Number up to 4 decimal points
      </td>
    </tr>

    <tr>
      <td>
        Apply fees to spread
      </td>

      <td>
        When enabled (you select yes), the spread is excluded from exchange transactions when calculating fee model taxes.

        Default: no (spread is included)

        For example: If the exchange rate is 1.3000 and the spread is 1.1205%, taxes will be calculated on 1.3000 if this setting is yes, not on the final conversion rate of 1.3146."
      </td>

      <td>
        `apply_fees_without_spread`
      </td>

      <td>
        boolean
      </td>

      <td>
        yes or no
      </td>
    </tr>

    <tr>
      <td>
        Conversion rate
      </td>

      <td>
        The exchange rate including the spread—a percentage markup added by the issuer.

        For example: If the exchange rate is 1.3000 and the spread is 1.1205%, the conversion rate is 1.3146.
      </td>

      <td>
        Auto-generated in Control Center
      </td>

      <td>
        number
      </td>

      <td>
        Auto-generated in Control Center
      </td>
    </tr>

    <tr>
      <td>
        Created time and date
      </td>

      <td>
        Timestamp when the request was created
      </td>

      <td>
        Auto-generated in Control Center
      </td>

      <td>
        short date
      </td>

      <td>
        Auto-generated in Control Center
      </td>
    </tr>

    <tr>
      <td>
        Date
      </td>

      <td>
        Today or tomorrow’s date in Coordinated Universal Time (UTC). If you have network acceptance for international purchases, you must register exchange rates daily.
      </td>

      <td>
        `date`
      </td>

      <td>
        short date
      </td>

      <td>
        YYYY-MM-DD
      </td>
    </tr>
  </tbody>
</Table>

# Create an exchange rate

To create a exchange rate:

1. From the main menu, select **Configurations** > **Exchange rates**.
2. On the **Exchange rates** screen, select **Create exchange rate**.
3. On the **Exchange rate details** screen, enter values for the fields described in the exchange rate field table above.
4. When you are done, select **Add exchange rate**.

# Bulk upload exchange rates

You can bulk upload exchange rates in a CSV file. First, select the link to download the spreadsheet. Complete the spreadsheet and then upload it using the **Bulk upload** button.

Refer to the table above for fields that need to be present in the CSV file. You don't need to enter the fields auto-generated by Control Center (**Conversion rate** and **Created time and date**).

**Note:** It is essential to include identity pairs when your setup is multi-currency.

> 📘 Separate fields with semi-colons (;) not commas
>
> Some of the exchange rate fields use commas. Both periods and commas work for the exchange rate and fee, regardless of the currency code. It is recommended to use one or the other for consistency.

**Sample bulk upload file:**

```
PROGRAM ID/ORG;DATE;EXCHANGE RATE;FEE (SPREAD);ORIGIN CURRENCY CODE;DESTINATION CURRENCY CODE;APPLY FEES WITHOUT SPREAD?
ORG;2025-09-23;1,0001;1,9999;USD;BRL;false
31776;2025-09-23;1,0021;1,9979;BRL;EUR;true
1865;2025-09-23;1,0022;1,9978;EUR;BRL;false
2070;2025-09-23;1,0071;1,9929;USD;EUR;false
```

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/exchange-rates` | `createExchangeRates` | Create exchange rate | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--exchange-rates |

### Operation essentials

- **`POST /v1/exchange-rates`** (`createExchangeRates`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `date`, `destination_currency_id`, `origin_currency_id`, `exchange_rate`, `spread`; response statuses 201, 400, 401, 422, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/control-center/exchange-rates.md`: updatedAt 2026-05-29T15:23:03.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/exchange-rates.md` | whole document | https://developers.pismo.io/pismo-docs/docs/exchange-rates | `a00b028f199e0a21…` | 2026-05-29T15:23:03.000Z |

## Related knowledge units

- `KU-API-platform-setup-rates-and-fees--exchange-rates` — API reference: Platform setup - Rates and fees — Exchange rates
- `KU-CORE-exchange-rate` — Exchange rates
