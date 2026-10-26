---
ku_id: KU-BANK-get-started-demand-deposit-accounts
title: Get started with demand deposit accounts (DDAs)
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/corporate-banking-launch-reference.md
  sha256: 7f3735781e85d6b84674b2f6e0728295dd312c5f05d4c02153a759c49ad01167
  url: https://developers.pismo.io/pismo-docs/docs/corporate-banking-launch-reference
  role: primary_guide
  updated_at: '2026-06-10T18:40:33.000Z'
- path: docs/get-started/get-started-building-demand-deposit-accounts.md
  sha256: 097e956d81a532607724d71a3574878a9612887b5e60ddb4e40afc1b274e62c0
  url: https://developers.pismo.io/pismo-docs/docs/get-started-building-demand-deposit-accounts
  role: primary_guide
  updated_at: '2026-06-29T19:37:33.000Z'
operations:
- CreateProgramBasedOnTemplate
- corporate-v2-post-payments
- corporate-v2-post-scheduled-payments
- get-accounts
- patch-division-v2
- post-account
- post-corporate-v2-earmarks
- post-division-v2
- post-hierarchies
- post-v1-accounts-flex-controls
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--hierarchies
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-platform-setup-programs--programs-part-01
- KU-BANK-calendars-and-holidays
- KU-BANK-divisions-and-hierarchies
- KU-BANK-earmarks
- KU-CORE-accounting-overview
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-account
- KU-EVT-catalogue-audit
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-GS-pismo-platform-onboarding
- KU-GS-setup-overview
- KU-PAY-payments-configurations
grouping_rationale: Identical bodies (duplicate pages).
---

# Get started with demand deposit accounts (DDAs)

**KU ID:** `KU-BANK-get-started-demand-deposit-accounts` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Identical bodies (duplicate pages).

Scope as stated in `docs/core-banking/corporate-banking-launch-reference.md`:

> To launch DDAs on the Pismo platform, you begin by working with the Pismo support team to create your organization (org) and a hierarchy of divisions within that org. Then you can set up programs and bind them to one or more divisions belonging to that org.

Scope as stated in `docs/get-started/get-started-building-demand-deposit-accounts.md`:

> To launch DDAs on the Pismo platform, you begin by working with the Pismo support team to create your organization (org) and a hierarchy of divisions within that org. Then you can set up programs and bind them to one or more divisions belonging to that org.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/corporate-banking-launch-reference.md`: Get started with demand deposit accounts (DDAs); Introduction; Step 1: Create your organization; Step 2: Set up a hierarchy; Step 3: Add divisions; Step 4: Set up holidays; Step 5: Set up an account schema for specific validations; Step 6: Set up your programs; Step 7: Bind your programs to divisions; Step 8: Set up processing codes; Step 9: Create flex controls using processing codes; Step 10: Configure accounting; Step 11: Create transaction account; Step 12: Retrieve account information; Balance types; Step 13: Perform operations; Cash-in; Cash-out; P2P transfer; Schedule a payment; Earmark funds
- `docs/get-started/get-started-building-demand-deposit-accounts.md`: Get started with demand deposit accounts (DDAs); Introduction; Step 1: Create your organization; Step 2: Set up a hierarchy; Step 3: Add divisions; Step 4: Set up holidays; Step 5: Set up an account schema for specific validations; Step 6: Set up your programs; Step 7: Bind your programs to divisions; Step 8: Set up processing codes; Step 9: Create flex controls using processing codes; Step 10: Configure accounting; Step 11: Create transaction account; Step 12: Retrieve account information; Balance types; Step 13: Perform operations; Cash-in; Cash-out; P2P transfer; Schedule a payment; Earmark funds

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/corporate-banking-launch-reference.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/corporate-banking-launch-reference · updatedAt: 2026-06-10T18:40:33.000Z

<!-- source:begin path=docs/core-banking/corporate-banking-launch-reference.md part=0-end -->

# Get started with demand deposit accounts (DDAs)

# Introduction

To launch DDAs on the Pismo platform, you begin by working with the Pismo support team to create your organization (org) and a hierarchy of divisions within that org. Then you can set up programs and bind them to one or more divisions belonging to that org.

The following table lists the components of DDAs at Pismo:

| Component                 | Single (S) or Multiple (M)\* | Required\*\* | Creation method                                    |
| :------------------------ | :--------------------------- | :----------- | :------------------------------------------------- |
| Organization (org)        | S                            | Y            | Pismo creates the org based on your specifications |
| Hierarchy                 | M                            | Y            | API                                                |
| Division                  | M                            | Y            | API                                                |
| Holiday                   | M                            | N            | API                                                |
| Account schema validation | M                            | N            | API                                                |
| Program                   | M                            | Y            | Pismo Console / API                                |
| Processing code           | M                            | Y            | API                                                |

* A component is considered single if you would normally have only one of them. A component is multiple if it's normal to have more than one. It's possible for a client to have only one program, for example, but most clients have more than one, so program is marked as multiple.

\*\* A component is considered required if the DDA product does not work without it. A component that is not technically required might still be required in practice because of local regulations or business rules.

The following sections describe how to set up these components.

# Step 1: Create your organization

An org is an object that represents your organization on the Pismo platform. Your Pismo support team creates your org. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 2: Set up a hierarchy

For transaction banking, you need to set up a hierarchy that describes the structure of your org. A hierarchy is made up of nested components called divisions. Those divisions are organized into levels, which correspond to categories such as geographical region, country, city, branch, etc.

An operation that affects a division also affects all the divisions that are nested within it. For example, suppose you have a level named “City” that contains a level named “Branch”. If you set up weekends as holidays for the City division “London”, then all the Branch divisions nested within the “London” division will treat weekends as holidays.

You set up a hierarchy by defining its levels using the [Create hierarchy levels](https://developers.pismo.io/pismo-docs/reference/post-hierarchies) endpoint. A level has a name, an index, and a description. The highest level within the hierarchy should have index 0, the next highest should have index 1, etc. When you first create a hierarchy, it consists of empty levels. You populate the levels with divisions in Step 3.

Most of the transaction banking endpoints act on divisions, and you have to create a hierarchy before you can create divisions, so this step is mandatory.

The following sample code shows how to use the endpoint to create the levels for a hierarchy:

```curl
curl --request POST  
     --url <https://api-sandbox.pismolabs.io/corporate/hierarchies>  
     --header 'Accept: application/json'  
     --header 'Content-Type: application/json'  
     --data '  
{  
     "levels": [  
          {  
               "index": 0,  
               "name": "Headquarters",  
               "description": "Root level"  
          },  
          {  
               "index": 1,  
               "name": "Region",  
               "description": "Regional level"  
          },  
          {  
               "index": 2,  
               "name": "Country",  
               "description": "Country level"  
          },  
          {  
               "index": 3,  
               "name": "City",  
               "description": "City level"  
          },  
          {  
               "index": 4,  
               "name": "Branch",  
               "description": "Branch level"  
          }  
     ],  
     "name": "Hierarchy One"  
}
```

If successful, the call returns a response similar to the following:

```json
{  
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",  
  "name": "Hierarchy One",  
  "levels": [  
    {  
      "id": "df48f983-c906-4bb3-83c7-ac2e18babb59",  
      "name": "Headquarters",  
      "index": 0,  
      "description": "Root level"  
    },  
    {  
      "id": "e7685dd9-e2c8-4a05-baf7-c7dd72c0969f",  
      "name": "Region",  
      "index": 1,  
      "description": "Regional level"  
    },  
    {  
      "id": "0b05d677-602f-4874-92ea-a23471573c67",  
      "name": "Country",  
      "index": 2,  
      "description": "Country level"  
    },  
    {  
      "id": "3cf5d1cf-e440-4813-ab14-7de22d2418e3",  
      "name": "City",  
      "index": 3,  
      "description": "City level"  
    },  
    {  
      "id": "22f4f976-11f2-451c-b62c-d4e2e174d90b",  
      "name": "Branch",  
      "index": 4,  
      "description": "Branch level"  
    }  
  ]  
}
```

Notice that the response includes an ID for each new level (and also one for the array).

For more information, refer to [Create hierarchies, levels, and divisions](https://developers.pismo.io/pismo-docs/docs/hierarchies-2#create-hierarchies-levels-and-divisions).

# Step 3: Add divisions

Divisions are the nested components that make up the structure of your org. Each division is assigned to a level. A division can contain other divisions, but only if they are at a lower level in the hierarchy.

For example, under a level named "Country", the divisions could be "United Kingdom", "Germany", "The United States", etc. Under the “United Kingdom” division, you might add City divisions, such as “London”, “Manchester”, etc. Under each City division, you might add Branch divisions.

Divisions are the components that actually make up a hierarchy. Levels are just a way of organizing them by type. So, adding divisions to the levels is a mandatory step. You use the ID of a level to add divisions to it. You add a division using the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint. This endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |

It also takes the following body parameters:

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                | Type   | Required |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- | :------- |
| id          | Unique identifier for the division. A unique value is automatically generated by the Pismo platform.                                                                                                                                                                                                                                                       | String | NM       |
| parent\_id  | Parent level division ID. If you don't include a parent ID, then the platform assumes the division doesn't have a parent, and it won't inherit the features of a parent. This should only be the case for divisions in the topmost level. It's your responsibility to ensure that all divisions that are not in the topmost level are assigned parent IDs. | String | N        |
| name        | Division name                                                                                                                                                                                                                                                                                                                                              | String | Y        |
| description | Division description                                                                                                                                                                                                                                                                                                                                       | String | N        |

A typical call to [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) looks something like this:

```curl
curl -X POST '<https://api-sandbox.pismolabs.io/corporate/hierarchies/><hierarchy ID>/levels/<level ID>/divisions' -H 'x-tenant: <Organization ID>' -H 'Content-Type: application/json' -d '{"parent_id": 1c6ca187-e61f-4301-8dcb-0e9749e89eef, "name": "London", "description": "LON - London City"}'
```

If successful, the call returns a response similar to this:

```json
{  
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",  
  "level_id": "3cb85fcc-c00c-4c83-ae89-cd2568531125",  
  "parent_id": "1c6ca187-e61f-4301-8dcb-0e9749e89eef",  
  "name": "London",  
  "description": "LON - London City"  
}
```

Notice that the response includes an ID for the new division.

A division element (for example, Country = "United Kingdom") can have a [parent/child relationship](https://developers.pismo.io/pismo-docs/reference/post-division-v2) with a division at a higher level. For example, “London” is not only a division element for the City level, it could also have “United Kingdom” as its parent division at the Country level. You define a division's parent division by putting the ID of the parent in the `parent_id` field. This field is mandatory for every division that is not in the topmost level. Divisions that are in the topmost level do not have parents, so `parent_id` is not required for them.

<Callout icon="📘" theme="info">
  **Note**

  Once a division is created, the Pismo platform schedules the cycle closing event according to the specified timezone. If no timezone is specified for the division, Pismo searches through each parent division up to the top level for a timezone configuration. If none of the parent divisions have a timezone set, Pismo defaults to using UTC for the division.
</Callout>

# Step 4: Set up holidays

For each division, you can set up holidays for the days on which you do not want to allow your customers to complete transactions. If you do not set up any holidays, transactions are allowed at any time, 24/7 - 365 days a year.

Organizations often need to block transactions on certain days for security or regulatory reasons. Brick and mortar branches, for example, might close on weekends and some holidays. Accepting transactions when no one is working could increase the regulatory and operational risk. Also, some countries only allow interest to accrue on business days. If an account holder is allowed to make a transaction on a non-business day, this can cause problems calculating interest.

You set up holidays using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint. This endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |
| divisionId  | Division ID  | String |

It takes the following body parameters:\*

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Type
      </th>

      <th>
        Required
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        holidays
      </td>

      <td>
        An array of objects.\
        Each object is defined by the next three rows:
      </td>

      <td>
        Array
      </td>

      <td>
        N
      </td>
    </tr>

    <tr>
      <td>
        holidays.day
      </td>

      <td>
        The day of the month on which the holiday takes place
      </td>

      <td>
        Integer
      </td>

      <td>
        Y (for each holiday)
      </td>
    </tr>

    <tr>
      <td>
        holidays.month
      </td>

      <td>
        The month in which the holiday takes place
      </td>

      <td>
        Integer
      </td>

      <td>
        Y (for each holiday)
      </td>
    </tr>

    <tr>
      <td>
        holidays.description
      </td>

      <td>
        A name or description for the holiday
      </td>

      <td>
        String
      </td>

      <td>
        N
      </td>
    </tr>

    <tr>
      <td>
        program\_ids
      </td>

      <td>
        The IDs of the programs that the holiday applies to. If no IDs are provided, the holiday applies to all the programs in the division.
      </td>

      <td>
        Array of integers
      </td>

      <td>
        N
      </td>
    </tr>
  </tbody>
</Table>

\*Fields not listed in the above table are not applicable to holidays.

Examples:

1. Define a holiday in the Temuco division. (Assume the path variables `hierarchyId`, `levelId`, and `divisionId` are set for Temuco.):
   ```curl
   curl --request PATCH '<https://api-sandbox.pismolabs.io/corporate/hierarchies/{hierarchyId}/levels/{levelId}/divisions/{divisionId}>'  
   --header 'x-tenant: {tenId}'  
   --header 'Content-Type: application/json'  
   --data-raw '{  
       "holidays": [  
           {"month": 2, "day": 2, "description": "Temuco festival"},  
           {"month": 2, "day": 3, "description": "Temuco festival"}  
       ],  
       "allow_weekends_transactions": false  
   }'
   ```

2. Define a holiday in the Chile division. (Assume the path variables `hierarchyId`, `levelId`, and `divisionId` are set for Chile.):
   ```curl
   curl --request PATCH '<https://api-sandbox.pismolabs.io/corporate/hierarchies/{hierarchyId}/levels/{levelId}/divisions/{divisionId}>'  
   --header 'x-tenant: {tenId}'  
   --header 'Content-Type: application/json'  
   --data-raw '{  
       "holidays": [  
           {"month": 3, "day": 15, "description": "Chile special date"}  
       ],  
       "allow_weekends_transactions": false  
   }'
   ```

<Callout icon="📘" theme="info">
  Since the `program_id` field is not included in the above requests, the holidays are applied to all programs in the specified divisions.
</Callout>

For more information, refer to [Calendars and holidays in transaction banking](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking)calendars-and-holidays-in-transaction-banking.

# Step 5: Set up an account schema for specific validations

You can store more information in a customer account than just the regular objects. To do this,  use the custom fields in the [Create transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint, which are inside the `applicant` object. If you need to perform specific validations on those custom fields, define those validations on the division where the account is located. You do this by defining the validation rules in a JSON schema and using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint to attach the schema to the division.

Using a JSON schema to validate custom fields is not mandatory, but it might be needed to meet local regulations and business rules. For example, you might have a business rule to retrieve a customer number from the applicant’s address confirmation document. You would need to set up a JSON schema to confirm that a number is retrieved from the document.

You set up an account schema using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint. This endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |
| divisionId  | Division ID  | String |

It takes the following body parameters:\*

| Parameter | Description                                                                                                                                                                                                                                             | Type | Required |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--- | :------- |
| schema    | An array of schemas. Each schema is a JSON value pair in the form: \[new Key]:\[new Value]. See the code snippet below for an example. Since you can use this endpoint for other things besides assigning a schema, the `schema` field is not required. | JSON | N        |

\*Fields not listed in the above table are not applicable to account schemas.

The following sample code shows how to use the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint to make the custom field `product_id` required:

```curl
curl --request PATCH \\ --url https\: //api-sandbox.pismolabs.io/corporate-beta/hierarchies/hierarchyId/levels/levelId/divisions/divisionId \--header 'Content-Type: application/json'  
--data ' {  
    "schema": {  
        "$schema": "<https://json-schema.org/draft/2020-12/schema>  

",  
        "$id": "<https://pismo.io/acquisitions.latam.schema.json>  

",  
        "title": "Schema validator for Chile V1",  
        "type": "object",  
        "properties": {  
            "product_id": {  
                "description": "The unique identifier for a product",  
                "type": "integer"  
            }  
        },  
        "required": [  
            "product_id"  
        ]  
    }  
}'
```

# Step 6: Set up your programs

Programs define the types of accounts a customer can open with your org, such as credit and debit accounts. You can't create customer accounts without at least one program, so this step is mandatory.

You can set up a program using Control Center. For more information, refer to [Program](https://developers.pismo.io/pismo-docs/docs/setup-overview#program).

Alternatively, you can set up a program using the API endpoint [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate). This endpoint takes the following fields:\*

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field Name
      </th>

      <th>
        Description
      </th>

      <th>
        Field Type
      </th>

      <th>
        Possible Values
      </th>

      <th>
        Required
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
      </td>

      <td>
        A name for the program
      </td>

      <td>
        String
      </td>

      <td />

      <td>
        Y
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        The type of program. (This indicates the template that Pismo uses behind the scenes.) Examples:

        * Current accounts
        * Internal accounts
        * Correspondent accounts
      </td>

      <td>
        String
      </td>

      <td>
        * CURRENT ACCOUNTS

        * INTERNAL ACCOUNTS

        * CORRESPONDENT ACCOUNTS
      </td>

      <td>
        Y
      </td>
    </tr>

    <tr>
      <td>
        timezone
      </td>

      <td>
        Program timezone
      </td>

      <td>
        String
      </td>

      <td />

      <td>
        Y
      </td>
    </tr>

    <tr>
      <td>
        currency\_numeric\_code
      </td>

      <td>
        Numeric code (ISO 4217) of the currency used by the program.
      </td>

      <td>
        String
      </td>

      <td />

      <td>
        Y
      </td>
    </tr>
  </tbody>
</Table>

\*Fields not listed in the above table are not applicable to transaction banking.

The following sample code shows how to use this endpoint to create a current accounts program named "Sample\_current\_accounts\_program":

```curl
curl --request POST  
     --url <https://api-sandbox.pismolabs.io/programs/v1/programs/template>  
     --header 'Accept: application/json'  
     --header 'Authorization: Bearer <your_bearer_token>'  
     --header 'Content-Type: application/json'  
     --data '  
{  
     "timezone": "America/Sao_Paulo",  
     "currency_numeric_code": "986",  
     "name": "Sample_current_accounts_program",  
     "type": "CURRENT ACCOUNTS"  
}'
```

# Step 7: Bind your programs to divisions

To use a program, it must be bound to at least one division. You bind programs to divisions using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint.

When you bind a program to a division, you tell the Pismo platform that accounts of that type can be opened in the division. You won’t be able to open any accounts until you bind at least one program to at least one division, so this step is mandatory.

You bind your programs using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint. A division can be bound to one program set (the group of programs that are available to a division). Refer to [Bind a program to a division](https://developers.pismo.io/pismo-docs/docs/hierarchies-2#bind-a-program-to-a-division).

<Callout icon="🚧" theme="warn">
  If you use [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) to bind a program set to a division, a subsequent call to this endpoint for the same division creates a new program set that effectively replaces the previous one.
</Callout>

The [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |
| divisionId  | Division ID  | String |

The [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint takes the following body parameter:\*

| Parameter    | Description | Type             |
| :----------- | :---------- | :--------------- |
| program\_ids | Program IDs | Array of strings |

\*Fields not listed in the above table are not applicable to program binding.

The following sample code shows how to bind a program to a division:

```curl
curl --request POST  
     --url <https://api-sandbox.pismolabs.io/corporate/corporate/hierarchies/{hierarchyId}/levels/{levelId}/divisions/{divisionId}/program-set>  
     --header 'Accept: application/json'  
     --header 'Content-Type: application/json'  
     --data '{  
     "program_ids": [  
          1214,  
          1215,  
          1225  
     ]  
}'
```

If successful, the call returns a response similar to this:

```json
{  
    204 no content  
}
```

# Step 8: Set up processing codes

A processing code is a numeric identifier that you can use to modify how Pismo handles certain transactions. Pismo provides a number of standard, predefined processing codes, but you can also add and configure your own codes.

Each code is associated with one or more transaction types. The standard processing code 220035 (CASHIN TRANSFER), for example, is associated with one transaction type 92000040 (CASHIN TRANSFER). The standard code 220037, however, is associated with three transaction types:

* 92000042 – CASHOUT TRANSFER
* 801 - CASHOUT WIRE TRANSFER FEE
* 412 - VALUE ADDED TAXES

Refer to [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) for more information and [Payments configurations](https://developers.pismo.io/pismo-docs/docs/payments-configurations) for a step by step guide.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Processing code
      </th>

      <th>
        Processing code description
      </th>

      <th>
        Available Balance impact
      </th>

      <th>
        Transaction type
      </th>

      <th>
        Transaction type description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        219248
      </td>

      <td>
        HOLD FUNDS
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        7128
      </td>

      <td>
        HOLD FUNDS
      </td>
    </tr>

    <tr>
      <td>
        219249
      </td>

      <td>
        HOLD FUNDS CANCEL
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000046
      </td>

      <td>
        HOLD FUNDS CANCE
      </td>
    </tr>

    <tr>
      <td>
        219250
      </td>

      <td>
        HOLD FUNDS UNDO CANCEL
      </td>

      <td>
        NEGATIVE
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        219251
      </td>

      <td>
        RELEASE FUNDS
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        7129
      </td>

      <td>
        RELEASE FUNDS
      </td>
    </tr>

    <tr>
      <td>
        219252
      </td>

      <td>
        RELEASE FUNDS CANCEL
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000047
      </td>

      <td>
        RELEASE FUNDS CANCEL
      </td>
    </tr>

    <tr>
      <td>
        219253
      </td>

      <td>
        RELEASE FUNDS UNDO CANCEL
      </td>

      <td>
        POSITIVE
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        220035
      </td>

      <td>
        CASHIN TRANSFER
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000040
      </td>

      <td>
        CASHIN TRANSFER
      </td>
    </tr>

    <tr>
      <td>
        220036
      </td>

      <td>
        UNDO CASHIN TRANSFER
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000041
      </td>

      <td>
        UNDO CASHIN TRANSFER
      </td>
    </tr>

    <tr>
      <td>
        220037
      </td>

      <td>
        CASHOUT TRANSFER
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000042

        801

        412
      </td>

      <td>
        CASHOUT TRANSFER

        CASHOUT WIRE TRANSFER FEE

        VALUE ADDED TAXES
      </td>
    </tr>

    <tr>
      <td>
        220038
      </td>

      <td>
        UNDO CASHOUT TRANSFER
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000043
      </td>

      <td>
        UNDO CASHOUT TRANSFER
      </td>
    </tr>

    <tr>
      <td>
        220039
      </td>

      <td>
        CREDIT ADJUSTMENT
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000044
      </td>

      <td>
        CREDIT ADJUSTMENT
      </td>
    </tr>

    <tr>
      <td>
        220040
      </td>

      <td>
        DEBIT ADJUSTMENT
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000045
      </td>

      <td>
        DEBIT ADJUSTMENT
      </td>
    </tr>
  </tbody>
</Table>

# Step 9: Create flex controls using processing codes

You create flex controls using the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) endpoint. You can use the processing code 220037, for example, to create a flex control that limits the amount of money an account can move in one cashout transaction.

# Step 10: Configure accounting

The Pismo platform provides tools to keep track of business and financial transactions for accounting purposes. There are five accounting elements in the Pismo platform:

* [Accounting scripts](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-script) – Accounting scripts determine what accounting entries the Pismo platform generates when an accounting event occurs. An accounting script, for example, should generate entries that show what debit account and credit account into which an amount flows. An organization can have one or more accounting scripts.
* [Accounting events](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-events) – The Pismo platform issues accounting events that impact your organization's records. Your accounting scripts determine the impact of each accounting event.
* [Accounting entries](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-entries) –  Accounting entries are the final product of the accounting events processing. These entries affect your organization's accounting records.
* [Accounting accounts](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-accounts) – Accounting accounts are the accounts from your organization's balance sheet. They keep a record of the funds in your general ledger. Each accounting script has two accounting accounts. One records your organization's assets, and the other records its liabilities.
* [Cost centers (optional)](https://developers.pismo.io/pismo-docs/docs/accounting-overview#cost-centers) – Cost centers are entities that cost an organization money or resources. Examples of a cost center are a human resources department or a revenue center.

You create accounting accounts and then configure accounting scripts to generate accounting entries based on accounting events.

Loans or credits extended by the bank to customers are considered the bank's assets, as customers are obligated to repay these amounts, often with interest. Conversely, deposits held by the bank are viewed as liabilities, as the bank is responsible for returning the customer's funds upon request.

If no interest is taken and no fee is charged for a transaction, the resulting balance of the operation, from an accounting standpoint, is zero for both assets and liabilities.

Cost centers are subdivisions of the balance sheet, but with a more operational view as opposed to the pure accounting view.

# Step 11: Create transaction account

You use the [Create corporate account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint to create a transaction account. This endpoint requires you to specify both a `division_id` and a `program_id`. The program specified by `program_id` must be bound to the division specified by `division_id`. For more information, refer to [Bind your programs to divisions](#step-7--bind-your-programs-to-divisions).

<Callout icon="🚧" theme="warn">
  You can only use the **Create account application** endpoint to create non-transaction banking accounts. Since transaction accounts must be associated with divisions, you need a special endpoint to create them.
</Callout>

# Step 12: Retrieve account information

You can retrieve information about a transaction account using the [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts) endpoint.

## Balance types

The [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts) endpoint returns several balance types:

* `available_balance` – Amount available for withdrawal (amount not earmarked)
* `book_balance` – Total amount in account (available\_balance + earmarked\_balance)
* `earmarked_balance` – Amount [earmarked](https://developers.pismo.io/pismo-docs/docs/earmarks) for settlement

If an action has an impact on the `available_balance`, the core platform domain issues a `change_available` event. For example:

```json
 {
	"arrival_epoch": 1667587104040,
	"event_id": "bcaa68bb-6159-4485-908d-f52d68570230",
	"timestamp": "2022-11-04T18:38:23.916776539Z",
	"domain": "availables",
	"event_type": "change_available",
	"schema_version": 1,
	"org_id": "TN-bc205a0c-11b8-4505-8668-f24a2af5123e",
	"cid": "85cc8e81-d7f9-90c8-ba7e-ca0eccfa74d7",
	"data": {
		"id": "e9f05dc8-2d6f-4623-906b-0acfc53467fb",
		"available_credit_limit": 632,
		"available_withdraw_limit": 0,
		"available_installment_limit": 0,
		"available_savings_account_limit": 0,
		"amount": 18,
		"amount_consider": 18,
		"tracking_id": "286186e4-2d9b-4fe4-a90b-e612-Cashout-debit",
		"account_id": 104436406,
		"org_id": "TN-bc205a0c-11b8-4505-8668-f24a2af5123e",
		"operation_type": "DEBIT",
		"updated_at": "2022-11-04 15:38:23.898503",
		"available_update_datetime": "2022-11-04T18:38:23Z",
		"caller": "p2ptransactions-api"
	}
}

```

The `amount` property shows that the value of the account balance increased by 18. (A positive amount indicates an increase.) The `available_credit_limit` is the credit limit for the account.

This transaction causes the transaction banking domain to issue a `balance_change` event. The balances communicated by this event are the resulting balances after the transaction impacted them. For example:

```json
{
	"event_id": "bcaa68bb-6159-4485-908d-f52d68570230",
	"timestamp": "2022-11-04T18:38:23.916776539Z",
	"domain": "account_balances",
	"event_type": "balance_change",
	"schema_version": 1,
	"org_id": "TN-bc205a0c-11b8-4505-8668-f24a2af5123e",
	"cid": "85cc8e81-d7f9-90c8-ba7e-ca0eccfa74d7",
	"data": {
    "id": "e9f05dc8-2d6f-4485-908d-f52d68570230",
    "account_id": 104436406,
    "operation_type": "DEBIT",
    "operation_amount": 18,
    "uncleared_funds": 0,
    "book_balance": 632,
    "earmarked_balance": 0,
    "available_balance": 0,
    "change_available_event_id": "e9f05dc8-2d6f-4623-906b-0acfc53467fb",	
    "tracking_id": "286186e4-2d9b-4fe4-a90b-e612-Cashout-debit",
    "balance_update_datetime": "2022-11-04T18:38:23Z"
  }
}

```

# Step 13: Perform operations

Endpoints **Initiate a payment** and **Schedule transactions** have the following optional arguments that are specific to transaction banking:

* `allow_suspense_posting`boolean\
  Defines if this transaction should be posted in suspense, in case it’s denied for any reason, such as lack of balance, account status, invalid currency, etc.
* `skip_account_date_validation`boolean\
  Defines if the transaction should be posted regardless of date validations. This parameter allows transactions to be back-dated beyond the account creation date and time.

Endpoint **[Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)** has the following optional argument that is specific to transaction banking:

* `expiry_datetime`date-time\
  ISO 8601 date/time for earmark release.

You can use the following operations to move funds between accounts.

## Cash-in

Use the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint to perform a cash-in operation. The following code shows how to perform a cash-in of 320 GBP on 2022-02-09.

<Callout icon="🚧" theme="warn">
  Currently, the maximum number of days supported for backdating is seven (7).
</Callout>

```curl
curl --location --request POST 'https://api-sandbox.pismolabs.io/corporate/payments' \
--header 'x-tenant: {tenantId}' \
--header 'Content-Type: application/json' \
--data-raw '{
	"descriptor": "Cash-in payment",
	"from": [
		{
			"custom_info": {
				"type": "CASHIN"
			}
		}
	],
	"to": [
		{
			"amount": 320,
			"currency": "GBP",
			"account": {
				"id": {accountId}
			}
		}
	],
    "payment_datetime": "2022-02-09T10:00:00Z",
}'
```

## Cash-out

Use the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint to perform a cash-out operation. The following code shows how to perform a cash-out of 400 GBP on 2022-02-07:

```curl
curl --location --request POST 'https://api-sandbox.pismolabs.io/corporate/payments' \
--header 'x-tenant: {tenantId}' \
--header 'Content-Type: application/json' \
--data-raw '{
	"descriptor": "Cash-out payment",
	"from": [
		{
			"amount": 400,
			"currency": "GBP",
			"account": {
				"id": {accountId}
			}
		}
	],
	"to": [
		{
			"custom_info": {
				"type": "CASHOUT"
			}
		}
	],
    "payment_datetime": "2022-02-07T10:00:00Z",
}'
```

## P2P transfer

Use the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint to perform a Pismo platform account to Pismo platform account (P2P) operation. The following code shows how to perform a P2P transfer of 100 GBP between two accounts on 2022-02-08:

```curl
curl --location --request POST 'https://api-sandbox.pismolabs.io/corporate/payments' \
--header 'x-tenant: {tenantId}' \
--header 'Content-Type: application/json' \
--data-raw '{
	"descriptor": "P2P payment",
	"from": [
		{
			"amount": 100,
			"currency": "GBP",
			"account": {
				"id": {accountId1}
			}
		}
	],
  "to": [
    {
    	"amount": 100,
			"currency": "GBP",
      "account": {
      	"id": {accountId2}
      }
    }
  ],
    "payment_datetime": "2022-02-08T10:00:00Z",
}'
```

## Schedule a payment

Use the [Scheduled payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments) endpoint to schedule a payment to occur at a future date and time. The endpoint performs validations to ensure that the scheduled date is in the future and does not occur on a holiday. The following code shows how to schedule a payment of 200 GBP for payment on 2024-04-10:

```curl
curl --request POST 'https://api-sandbox.pismolabs.io/corporate/payments/schedules' 
-H 'x-tenant: <organization ID>' -H 'Content-Type: application/json' 
-d '{
    "descriptor": "P2P payment",
    "from": [
        {
            "custom_info": {
                "type": "CASHIN",
                "external_id": "e731652e-87d5-4acb-8f32-cb5cfd095a12"
            }
        }
    ],
    "to": [
        {
            "amount": 200,
            "currency": "GBP",
            "account": {
                "id": {accountId}
            }
        }
    ],
    "payment_datetime": "2024-04-10T15:00:00Z"
}'
```

For more information, refer to [Scheduled payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments).

## Earmark funds

Use the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint to earmark funds for a future cash-out (usually a payment). The difference between scheduling a payment and earmarking funds for a payment is that earmarking the funds holds them in reserve, so that they cannot be withdrawn from the account before the payment.

The following code shows how to earmark 50 USD for payment on 2024-04-10:

```curl
curl --request POST \
     --url https://api-sandbox.pismolabs.io/corporate/earmarks \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --data '
{
     "from": {
          "account": {
               "id": "102701621"
          },
          "amount": 50,
          "currency": "USD"
     },
     "to": {
          "custom_info": {
               "type": "Scheduled earmark",
               "external_id": "123ABC"
          }
     },
     "tracking_id": "ABC123",
     "descriptor": "Hold Funds",
     "expiry_datetime": "2024-04-10T15:00:00Z"
}
'
```

For more information, refer to [Earmarks](https://developers.pismo.io/pismo-docs/docs/earmarks).

<br />
<!-- source:end -->

### Source 2: `docs/get-started/get-started-building-demand-deposit-accounts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-building-demand-deposit-accounts · updatedAt: 2026-06-29T19:37:33.000Z

<!-- source:begin path=docs/get-started/get-started-building-demand-deposit-accounts.md part=0-end -->

# Get started with demand deposit accounts (DDAs) 

# Introduction

To launch DDAs on the Pismo platform, you begin by working with the Pismo support team to create your organization (org) and a hierarchy of divisions within that org. Then you can set up programs and bind them to one or more divisions belonging to that org.

The following table lists the components of DDAs at Pismo:

| Component                 | Single (S) or Multiple (M)\* | Required\*\* | Creation method                                    |
| :------------------------ | :--------------------------- | :----------- | :------------------------------------------------- |
| Organization (org)        | S                            | Y            | Pismo creates the org based on your specifications |
| Hierarchy                 | M                            | Y            | API                                                |
| Division                  | M                            | Y            | API                                                |
| Holiday                   | M                            | N            | API                                                |
| Account schema validation | M                            | N            | API                                                |
| Program                   | M                            | Y            | Pismo Console / API                                |
| Processing code           | M                            | Y            | API                                                |

* A component is considered single if you would normally have only one of them. A component is multiple if it's normal to have more than one. It's possible for a client to have only one program, for example, but most clients have more than one, so program is marked as multiple.

\*\* A component is considered required if the DDA product does not work without it. A component that is not technically required might still be required in practice because of local regulations or business rules.

The following sections describe how to set up these components.

# Step 1: Create your organization

An org is an object that represents your organization on the Pismo platform. Your Pismo support team creates your org. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 2: Set up a hierarchy

For transaction banking, you need to set up a hierarchy that describes the structure of your org. A hierarchy is made up of nested components called divisions. Those divisions are organized into levels, which correspond to categories such as geographical region, country, city, branch, etc.

An operation that affects a division also affects all the divisions that are nested within it. For example, suppose you have a level named “City” that contains a level named “Branch”. If you set up weekends as holidays for the City division “London”, then all the Branch divisions nested within the “London” division will treat weekends as holidays.

You set up a hierarchy by defining its levels using the [Create hierarchy levels](https://developers.pismo.io/pismo-docs/reference/post-hierarchies) endpoint. A level has a name, an index, and a description. The highest level within the hierarchy should have index 0, the next highest should have index 1, etc. When you first create a hierarchy, it consists of empty levels. You populate the levels with divisions in Step 3.

Most of the transaction banking endpoints act on divisions, and you have to create a hierarchy before you can create divisions, so this step is mandatory.

The following sample code shows how to use the endpoint to create the levels for a hierarchy:

```curl
curl --request POST  
     --url <https://api-sandbox.pismolabs.io/corporate/hierarchies>  
     --header 'Accept: application/json'  
     --header 'Content-Type: application/json'  
     --data '  
{  
     "levels": [  
          {  
               "index": 0,  
               "name": "Headquarters",  
               "description": "Root level"  
          },  
          {  
               "index": 1,  
               "name": "Region",  
               "description": "Regional level"  
          },  
          {  
               "index": 2,  
               "name": "Country",  
               "description": "Country level"  
          },  
          {  
               "index": 3,  
               "name": "City",  
               "description": "City level"  
          },  
          {  
               "index": 4,  
               "name": "Branch",  
               "description": "Branch level"  
          }  
     ],  
     "name": "Hierarchy One"  
}
```

If successful, the call returns a response similar to the following:

```json
{  
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",  
  "name": "Hierarchy One",  
  "levels": [  
    {  
      "id": "df48f983-c906-4bb3-83c7-ac2e18babb59",  
      "name": "Headquarters",  
      "index": 0,  
      "description": "Root level"  
    },  
    {  
      "id": "e7685dd9-e2c8-4a05-baf7-c7dd72c0969f",  
      "name": "Region",  
      "index": 1,  
      "description": "Regional level"  
    },  
    {  
      "id": "0b05d677-602f-4874-92ea-a23471573c67",  
      "name": "Country",  
      "index": 2,  
      "description": "Country level"  
    },  
    {  
      "id": "3cf5d1cf-e440-4813-ab14-7de22d2418e3",  
      "name": "City",  
      "index": 3,  
      "description": "City level"  
    },  
    {  
      "id": "22f4f976-11f2-451c-b62c-d4e2e174d90b",  
      "name": "Branch",  
      "index": 4,  
      "description": "Branch level"  
    }  
  ]  
}
```

Notice that the response includes an ID for each new level (and also one for the array).

For more information, refer to [Create hierarchies, levels, and divisions](https://developers.pismo.io/pismo-docs/docs/hierarchies-2#create-hierarchies-levels-and-divisions).

# Step 3: Add divisions

Divisions are the nested components that make up the structure of your org. Each division is assigned to a level. A division can contain other divisions, but only if they are at a lower level in the hierarchy.

For example, under a level named "Country", the divisions could be "United Kingdom", "Germany", "The United States", etc. Under the “United Kingdom” division, you might add City divisions, such as “London”, “Manchester”, etc. Under each City division, you might add Branch divisions.

Divisions are the components that actually make up a hierarchy. Levels are just a way of organizing them by type. So, adding divisions to the levels is a mandatory step. You use the ID of a level to add divisions to it. You add a division using the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint. This endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |

It also takes the following body parameters:

| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                | Type   | Required |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- | :------- |
| id          | Unique identifier for the division. A unique value is automatically generated by the Pismo platform.                                                                                                                                                                                                                                                       | String | NM       |
| parent\_id  | Parent level division ID. If you don't include a parent ID, then the platform assumes the division doesn't have a parent, and it won't inherit the features of a parent. This should only be the case for divisions in the topmost level. It's your responsibility to ensure that all divisions that are not in the topmost level are assigned parent IDs. | String | N        |
| name        | Division name                                                                                                                                                                                                                                                                                                                                              | String | Y        |
| description | Division description                                                                                                                                                                                                                                                                                                                                       | String | N        |

A typical call to [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) looks something like this:

```curl
curl -X POST '<https://api-sandbox.pismolabs.io/corporate/hierarchies/><hierarchy ID>/levels/<level ID>/divisions' -H 'x-tenant: <Organization ID>' -H 'Content-Type: application/json' -d '{"parent_id": 1c6ca187-e61f-4301-8dcb-0e9749e89eef, "name": "London", "description": "LON - London City"}'
```

If successful, the call returns a response similar to this:

```json
{  
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",  
  "level_id": "3cb85fcc-c00c-4c83-ae89-cd2568531125",  
  "parent_id": "1c6ca187-e61f-4301-8dcb-0e9749e89eef",  
  "name": "London",  
  "description": "LON - London City"  
}
```

Notice that the response includes an ID for the new division.

A division element (for example, Country = "United Kingdom") can have a [parent/child relationship](https://developers.pismo.io/pismo-docs/reference/post-division-v2) with a division at a higher level. For example, “London” is not only a division element for the City level, it could also have “United Kingdom” as its parent division at the Country level. You define a division's parent division by putting the ID of the parent in the `parent_id` field. This field is mandatory for every division that is not in the topmost level. Divisions that are in the topmost level do not have parents, so `parent_id` is not required for them.

<Callout icon="📘" theme="info">
  **Note**

  Once a division is created, the Pismo platform schedules the cycle closing event according to the specified timezone. If no timezone is specified for the division, Pismo searches through each parent division up to the top level for a timezone configuration. If none of the parent divisions have a timezone set, Pismo defaults to using UTC for the division.
</Callout>

# Step 4: Set up holidays

For each division, you can set up holidays for the days on which you do not want to allow your customers to complete transactions. If you do not set up any holidays, transactions are allowed at any time, 24/7 - 365 days a year.

Organizations often need to block transactions on certain days for security or regulatory reasons. Brick and mortar branches, for example, might close on weekends and some holidays. Accepting transactions when no one is working could increase the regulatory and operational risk. Also, some countries only allow interest to accrue on business days. If an account holder is allowed to make a transaction on a non-business day, this can cause problems calculating interest.

You set up holidays using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint. This endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |
| divisionId  | Division ID  | String |

It takes the following body parameters:\*

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Type
      </th>

      <th>
        Required
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        holidays
      </td>

      <td>
        An array of objects.\
        Each object is defined by the next three rows:
      </td>

      <td>
        Array
      </td>

      <td>
        N
      </td>
    </tr>

    <tr>
      <td>
        holidays.day
      </td>

      <td>
        The day of the month on which the holiday takes place
      </td>

      <td>
        Integer
      </td>

      <td>
        Y (for each holiday)
      </td>
    </tr>

    <tr>
      <td>
        holidays.month
      </td>

      <td>
        The month in which the holiday takes place
      </td>

      <td>
        Integer
      </td>

      <td>
        Y (for each holiday)
      </td>
    </tr>

    <tr>
      <td>
        holidays.description
      </td>

      <td>
        A name or description for the holiday
      </td>

      <td>
        String
      </td>

      <td>
        N
      </td>
    </tr>

    <tr>
      <td>
        program\_ids
      </td>

      <td>
        The IDs of the programs that the holiday applies to. If no IDs are provided, the holiday applies to all the programs in the division.
      </td>

      <td>
        Array of integers
      </td>

      <td>
        N
      </td>
    </tr>
  </tbody>
</Table>

\*Fields not listed in the above table are not applicable to holidays.

Examples:

1. Define a holiday in the Temuco division. (Assume the path variables `hierarchyId`, `levelId`, and `divisionId` are set for Temuco.):
   ```curl
   curl --request PATCH '<https://api-sandbox.pismolabs.io/corporate/hierarchies/{hierarchyId}/levels/{levelId}/divisions/{divisionId}>'  
   --header 'x-tenant: {tenId}'  
   --header 'Content-Type: application/json'  
   --data-raw '{  
       "holidays": [  
           {"month": 2, "day": 2, "description": "Temuco festival"},  
           {"month": 2, "day": 3, "description": "Temuco festival"}  
       ],  
       "allow_weekends_transactions": false  
   }'
   ```

2. Define a holiday in the Chile division. (Assume the path variables `hierarchyId`, `levelId`, and `divisionId` are set for Chile.):
   ```curl
   curl --request PATCH '<https://api-sandbox.pismolabs.io/corporate/hierarchies/{hierarchyId}/levels/{levelId}/divisions/{divisionId}>'  
   --header 'x-tenant: {tenId}'  
   --header 'Content-Type: application/json'  
   --data-raw '{  
       "holidays": [  
           {"month": 3, "day": 15, "description": "Chile special date"}  
       ],  
       "allow_weekends_transactions": false  
   }'
   ```

<Callout icon="📘" theme="info">
  Since the `program_id` field is not included in the above requests, the holidays are applied to all programs in the specified divisions.
</Callout>

For more information, refer to [Calendars and holidays in transaction banking](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-transaction-banking)calendars-and-holidays-in-transaction-banking.

# Step 5: Set up an account schema for specific validations

You can store more information in a customer account than just the regular objects. To do this,  use the custom fields in the [Create transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint, which are inside the `applicant` object. If you need to perform specific validations on those custom fields, define those validations on the division where the account is located. You do this by defining the validation rules in a JSON schema and using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint to attach the schema to the division.

Using a JSON schema to validate custom fields is not mandatory, but it might be needed to meet local regulations and business rules. For example, you might have a business rule to retrieve a customer number from the applicant’s address confirmation document. You would need to set up a JSON schema to confirm that a number is retrieved from the document.

You set up an account schema using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint. This endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |
| divisionId  | Division ID  | String |

It takes the following body parameters:\*

| Parameter | Description                                                                                                                                                                                                                                             | Type | Required |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--- | :------- |
| schema    | An array of schemas. Each schema is a JSON value pair in the form: \[new Key]:\[new Value]. See the code snippet below for an example. Since you can use this endpoint for other things besides assigning a schema, the `schema` field is not required. | JSON | N        |

\*Fields not listed in the above table are not applicable to account schemas.

The following sample code shows how to use the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint to make the custom field `product_id` required:

```curl
curl --request PATCH \\ --url https\: //api-sandbox.pismolabs.io/corporate-beta/hierarchies/hierarchyId/levels/levelId/divisions/divisionId \--header 'Content-Type: application/json'  
--data ' {  
    "schema": {  
        "$schema": "<https://json-schema.org/draft/2020-12/schema>  

",  
        "$id": "<https://pismo.io/acquisitions.latam.schema.json>  

",  
        "title": "Schema validator for Chile V1",  
        "type": "object",  
        "properties": {  
            "product_id": {  
                "description": "The unique identifier for a product",  
                "type": "integer"  
            }  
        },  
        "required": [  
            "product_id"  
        ]  
    }  
}'
```

# Step 6: Set up your programs

Programs define the types of accounts a customer can open with your org, such as credit and debit accounts. You can't create customer accounts without at least one program, so this step is mandatory.

You can set up a program using Control Center. For more information, refer to [Program](https://developers.pismo.io/pismo-docs/docs/setup-overview#program).

Alternatively, you can set up a program using the API endpoint [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate). This endpoint takes the following fields:\*

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field Name
      </th>

      <th>
        Description
      </th>

      <th>
        Field Type
      </th>

      <th>
        Possible Values
      </th>

      <th>
        Required
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
      </td>

      <td>
        A name for the program
      </td>

      <td>
        String
      </td>

      <td />

      <td>
        Y
      </td>
    </tr>

    <tr>
      <td>
        type
      </td>

      <td>
        The type of program. (This indicates the template that Pismo uses behind the scenes.) Examples:

        * Current accounts
        * Internal accounts
        * Correspondent accounts
      </td>

      <td>
        String
      </td>

      <td>
        * CURRENT ACCOUNTS

        * INTERNAL ACCOUNTS

        * CORRESPONDENT ACCOUNTS
      </td>

      <td>
        Y
      </td>
    </tr>

    <tr>
      <td>
        timezone
      </td>

      <td>
        Program timezone
      </td>

      <td>
        String
      </td>

      <td />

      <td>
        Y
      </td>
    </tr>

    <tr>
      <td>
        currency\_numeric\_code
      </td>

      <td>
        Numeric code (ISO 4217) of the currency used by the program.
      </td>

      <td>
        String
      </td>

      <td />

      <td>
        Y
      </td>
    </tr>
  </tbody>
</Table>

\*Fields not listed in the above table are not applicable to transaction banking.

The following sample code shows how to use this endpoint to create a current accounts program named "Sample\_current\_accounts\_program":

```curl
curl --request POST  
     --url <https://api-sandbox.pismolabs.io/programs/v1/programs/template>  
     --header 'Accept: application/json'  
     --header 'Authorization: Bearer <your_bearer_token>'  
     --header 'Content-Type: application/json'  
     --data '  
{  
     "timezone": "America/Sao_Paulo",  
     "currency_numeric_code": "986",  
     "name": "Sample_current_accounts_program",  
     "type": "CURRENT ACCOUNTS"  
}'
```

# Step 7: Bind your programs to divisions

To use a program, it must be bound to at least one division. You bind programs to divisions using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint.

When you bind a program to a division, you tell the Pismo platform that accounts of that type can be opened in the division. You won’t be able to open any accounts until you bind at least one program to at least one division, so this step is mandatory.

You bind your programs using the [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint. A division can be bound to one program set (the group of programs that are available to a division). Refer to [Bind a program to a division](https://developers.pismo.io/pismo-docs/docs/hierarchies-2#bind-a-program-to-a-division).

<Callout icon="🚧" theme="warn">
  If you use [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) to bind a program set to a division, a subsequent call to this endpoint for the same division creates a new program set that effectively replaces the previous one.
</Callout>

The [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint requires the following path parameters:

| Parameter   | Description  | Type   |
| :---------- | :----------- | :----- |
| hierarchyId | Hierarchy ID | String |
| levelId     | Level ID     | String |
| divisionId  | Division ID  | String |

The [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoint takes the following body parameter:\*

| Parameter    | Description | Type             |
| :----------- | :---------- | :--------------- |
| program\_ids | Program IDs | Array of strings |

\*Fields not listed in the above table are not applicable to program binding.

The following sample code shows how to bind a program to a division:

```curl
curl --request POST  
     --url <https://api-sandbox.pismolabs.io/corporate/corporate/hierarchies/{hierarchyId}/levels/{levelId}/divisions/{divisionId}/program-set>  
     --header 'Accept: application/json'  
     --header 'Content-Type: application/json'  
     --data '{  
     "program_ids": [  
          1214,  
          1215,  
          1225  
     ]  
}'
```

If successful, the call returns a response similar to this:

```json
{  
    204 no content  
}
```

# Step 8: Set up processing codes

A processing code is a numeric identifier that you can use to modify how Pismo handles certain transactions. Pismo provides a number of standard, predefined processing codes, but you can also add and configure your own codes.

Each code is associated with one or more transaction types. The standard processing code 220035 (CASHIN TRANSFER), for example, is associated with one transaction type 92000040 (CASHIN TRANSFER). The standard code 220037, however, is associated with three transaction types:

* 92000042 – CASHOUT TRANSFER
* 801 - CASHOUT WIRE TRANSFER FEE
* 412 - VALUE ADDED TAXES

Refer to [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) for more information and [Payments configurations](https://developers.pismo.io/pismo-docs/docs/payments-configurations) for a step by step guide.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Processing code
      </th>

      <th>
        Processing code description
      </th>

      <th>
        Available Balance impact
      </th>

      <th>
        Transaction type
      </th>

      <th>
        Transaction type description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        219248
      </td>

      <td>
        HOLD FUNDS
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        7128
      </td>

      <td>
        HOLD FUNDS
      </td>
    </tr>

    <tr>
      <td>
        219249
      </td>

      <td>
        HOLD FUNDS CANCEL
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000046
      </td>

      <td>
        HOLD FUNDS CANCE
      </td>
    </tr>

    <tr>
      <td>
        219250
      </td>

      <td>
        HOLD FUNDS UNDO CANCEL
      </td>

      <td>
        NEGATIVE
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        219251
      </td>

      <td>
        RELEASE FUNDS
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        7129
      </td>

      <td>
        RELEASE FUNDS
      </td>
    </tr>

    <tr>
      <td>
        219252
      </td>

      <td>
        RELEASE FUNDS CANCEL
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000047
      </td>

      <td>
        RELEASE FUNDS CANCEL
      </td>
    </tr>

    <tr>
      <td>
        219253
      </td>

      <td>
        RELEASE FUNDS UNDO CANCEL
      </td>

      <td>
        POSITIVE
      </td>

      <td />

      <td />
    </tr>

    <tr>
      <td>
        220035
      </td>

      <td>
        CASHIN TRANSFER
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000040
      </td>

      <td>
        CASHIN TRANSFER
      </td>
    </tr>

    <tr>
      <td>
        220036
      </td>

      <td>
        UNDO CASHIN TRANSFER
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000041
      </td>

      <td>
        UNDO CASHIN TRANSFER
      </td>
    </tr>

    <tr>
      <td>
        220037
      </td>

      <td>
        CASHOUT TRANSFER
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000042

        801

        412
      </td>

      <td>
        CASHOUT TRANSFER

        CASHOUT WIRE TRANSFER FEE

        VALUE ADDED TAXES
      </td>
    </tr>

    <tr>
      <td>
        220038
      </td>

      <td>
        UNDO CASHOUT TRANSFER
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000043
      </td>

      <td>
        UNDO CASHOUT TRANSFER
      </td>
    </tr>

    <tr>
      <td>
        220039
      </td>

      <td>
        CREDIT ADJUSTMENT
      </td>

      <td>
        POSITIVE
      </td>

      <td>
        92000044
      </td>

      <td>
        CREDIT ADJUSTMENT
      </td>
    </tr>

    <tr>
      <td>
        220040
      </td>

      <td>
        DEBIT ADJUSTMENT
      </td>

      <td>
        NEGATIVE
      </td>

      <td>
        92000045
      </td>

      <td>
        DEBIT ADJUSTMENT
      </td>
    </tr>
  </tbody>
</Table>

# Step 9: Create flex controls using processing codes

You create flex controls using the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) endpoint. You can use the processing code 220037, for example, to create a flex control that limits the amount of money an account can move in one cashout transaction.

# Step 10: Configure accounting

The Pismo platform provides tools to keep track of business and financial transactions for accounting purposes. There are five accounting elements in the Pismo platform:

* [Accounting scripts](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-script) – Accounting scripts determine what accounting entries the Pismo platform generates when an accounting event occurs. An accounting script, for example, should generate entries that show what debit account and credit account into which an amount flows. An organization can have one or more accounting scripts.
* [Accounting events](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-events) – The Pismo platform issues accounting events that impact your organization's records. Your accounting scripts determine the impact of each accounting event.
* [Accounting entries](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-entries) –  Accounting entries are the final product of the accounting events processing. These entries affect your organization's accounting records.
* [Accounting accounts](https://developers.pismo.io/pismo-docs/docs/accounting-overview#accounting-accounts) – Accounting accounts are the accounts from your organization's balance sheet. They keep a record of the funds in your general ledger. Each accounting script has two accounting accounts. One records your organization's assets, and the other records its liabilities.
* [Cost centers (optional)](https://developers.pismo.io/pismo-docs/docs/accounting-overview#cost-centers) – Cost centers are entities that cost an organization money or resources. Examples of a cost center are a human resources department or a revenue center.

You create accounting accounts and then configure accounting scripts to generate accounting entries based on accounting events.

Loans or credits extended by the bank to customers are considered the bank's assets, as customers are obligated to repay these amounts, often with interest. Conversely, deposits held by the bank are viewed as liabilities, as the bank is responsible for returning the customer's funds upon request.

If no interest is taken and no fee is charged for a transaction, the resulting balance of the operation, from an accounting standpoint, is zero for both assets and liabilities.

Cost centers are subdivisions of the balance sheet, but with a more operational view as opposed to the pure accounting view.

# Step 11: Create transaction account

You use the [Create corporate account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint to create a transaction account. This endpoint requires you to specify both a `division_id` and a `program_id`. The program specified by `program_id` must be bound to the division specified by `division_id`. For more information, refer to [Bind your programs to divisions](#step-7--bind-your-programs-to-divisions).

<Callout icon="🚧" theme="warn">
  You can only use the **Create account application** endpoint to create non-transaction banking accounts. Since transaction accounts must be associated with divisions, you need a special endpoint to create them.
</Callout>

# Step 12: Retrieve account information

You can retrieve information about a transaction account using the [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts) endpoint.

## Balance types

The [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts) endpoint returns several balance types:

* `available_balance` – Amount available for withdrawal (amount not earmarked)
* `book_balance` – Total amount in account (available\_balance + earmarked\_balance)
* `earmarked_balance` – Amount [earmarked](https://developers.pismo.io/pismo-docs/docs/earmarks) for settlement

If an action has an impact on the `available_balance`, the core platform domain issues a `change_available` event. For example:

```json
 {
	"arrival_epoch": 1667587104040,
	"event_id": "bcaa68bb-6159-4485-908d-f52d68570230",
	"timestamp": "2022-11-04T18:38:23.916776539Z",
	"domain": "availables",
	"event_type": "change_available",
	"schema_version": 1,
	"org_id": "TN-bc205a0c-11b8-4505-8668-f24a2af5123e",
	"cid": "85cc8e81-d7f9-90c8-ba7e-ca0eccfa74d7",
	"data": {
		"id": "e9f05dc8-2d6f-4623-906b-0acfc53467fb",
		"available_credit_limit": 632,
		"available_withdraw_limit": 0,
		"available_installment_limit": 0,
		"available_savings_account_limit": 0,
		"amount": 18,
		"amount_consider": 18,
		"tracking_id": "286186e4-2d9b-4fe4-a90b-e612-Cashout-debit",
		"account_id": 104436406,
		"org_id": "TN-bc205a0c-11b8-4505-8668-f24a2af5123e",
		"operation_type": "DEBIT",
		"updated_at": "2022-11-04 15:38:23.898503",
		"available_update_datetime": "2022-11-04T18:38:23Z",
		"caller": "p2ptransactions-api"
	}
}

```

The `amount` property shows that the value of the account balance increased by 18. (A positive amount indicates an increase.) The `available_credit_limit` is the credit limit for the account.

This transaction causes the transaction banking domain to issue a `balance_change` event. The balances communicated by this event are the resulting balances after the transaction impacted them. For example:

```json
{
	"event_id": "bcaa68bb-6159-4485-908d-f52d68570230",
	"timestamp": "2022-11-04T18:38:23.916776539Z",
	"domain": "account_balances",
	"event_type": "balance_change",
	"schema_version": 1,
	"org_id": "TN-bc205a0c-11b8-4505-8668-f24a2af5123e",
	"cid": "85cc8e81-d7f9-90c8-ba7e-ca0eccfa74d7",
	"data": {
    "id": "e9f05dc8-2d6f-4485-908d-f52d68570230",
    "account_id": 104436406,
    "operation_type": "DEBIT",
    "operation_amount": 18,
    "uncleared_funds": 0,
    "book_balance": 632,
    "earmarked_balance": 0,
    "available_balance": 0,
    "change_available_event_id": "e9f05dc8-2d6f-4623-906b-0acfc53467fb",	
    "tracking_id": "286186e4-2d9b-4fe4-a90b-e612-Cashout-debit",
    "balance_update_datetime": "2022-11-04T18:38:23Z"
  }
}

```

# Step 13: Perform operations

Endpoints **Initiate a payment** and **Schedule transactions** have the following optional arguments that are specific to transaction banking:

* `allow_suspense_posting`boolean\
  Defines if this transaction should be posted in suspense, in case it’s denied for any reason, such as lack of balance, account status, invalid currency, etc.
* `skip_account_date_validation`boolean\
  Defines if the transaction should be posted regardless of date validations. This parameter allows transactions to be back-dated beyond the account creation date and time.

Endpoint **[Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)** has the following optional argument that is specific to transaction banking:

* `expiry_datetime`date-time\
  ISO 8601 date/time for earmark release.

You can use the following operations to move funds between accounts.

## Cash-in

Use the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint to perform a cash-in operation. The following code shows how to perform a cash-in of 320 GBP on 2022-02-09.

<Callout icon="🚧" theme="warn">
  Currently, the maximum number of days supported for backdating is seven (7).
</Callout>

```curl
curl --location --request POST 'https://api-sandbox.pismolabs.io/corporate/payments' \
--header 'x-tenant: {tenantId}' \
--header 'Content-Type: application/json' \
--data-raw '{
	"descriptor": "Cash-in payment",
	"from": [
		{
			"custom_info": {
				"type": "CASHIN"
			}
		}
	],
	"to": [
		{
			"amount": 320,
			"currency": "GBP",
			"account": {
				"id": {accountId}
			}
		}
	],
    "payment_datetime": "2022-02-09T10:00:00Z",
}'
```

## Cash-out

Use the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint to perform a cash-out operation. The following code shows how to perform a cash-out of 400 GBP on 2022-02-07:

```curl
curl --location --request POST 'https://api-sandbox.pismolabs.io/corporate/payments' \
--header 'x-tenant: {tenantId}' \
--header 'Content-Type: application/json' \
--data-raw '{
	"descriptor": "Cash-out payment",
	"from": [
		{
			"amount": 400,
			"currency": "GBP",
			"account": {
				"id": {accountId}
			}
		}
	],
	"to": [
		{
			"custom_info": {
				"type": "CASHOUT"
			}
		}
	],
    "payment_datetime": "2022-02-07T10:00:00Z",
}'
```

## P2P transfer

Use the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint to perform a Pismo platform account to Pismo platform account (P2P) operation. The following code shows how to perform a P2P transfer of 100 GBP between two accounts on 2022-02-08:

```curl
curl --location --request POST 'https://api-sandbox.pismolabs.io/corporate/payments' \
--header 'x-tenant: {tenantId}' \
--header 'Content-Type: application/json' \
--data-raw '{
	"descriptor": "P2P payment",
	"from": [
		{
			"amount": 100,
			"currency": "GBP",
			"account": {
				"id": {accountId1}
			}
		}
	],
  "to": [
    {
    	"amount": 100,
			"currency": "GBP",
      "account": {
      	"id": {accountId2}
      }
    }
  ],
    "payment_datetime": "2022-02-08T10:00:00Z",
}'
```

## Schedule a payment

Use the [Scheduled payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments) endpoint to schedule a payment to occur at a future date and time. The endpoint performs validations to ensure that the scheduled date is in the future and does not occur on a holiday. The following code shows how to schedule a payment of 200 GBP for payment on 2024-04-10:

```curl
curl --request POST 'https://api-sandbox.pismolabs.io/corporate/payments/schedules' 
-H 'x-tenant: <organization ID>' -H 'Content-Type: application/json' 
-d '{
    "descriptor": "P2P payment",
    "from": [
        {
            "custom_info": {
                "type": "CASHIN",
                "external_id": "e731652e-87d5-4acb-8f32-cb5cfd095a12"
            }
        }
    ],
    "to": [
        {
            "amount": 200,
            "currency": "GBP",
            "account": {
                "id": {accountId}
            }
        }
    ],
    "payment_datetime": "2024-04-10T15:00:00Z"
}'
```

For more information, refer to [Scheduled payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments).

## Earmark funds

Use the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint to earmark funds for a future cash-out (usually a payment). The difference between scheduling a payment and earmarking funds for a payment is that earmarking the funds holds them in reserve, so that they cannot be withdrawn from the account before the payment.

The following code shows how to earmark 50 USD for payment on 2024-04-10:

```curl
curl --request POST \
     --url https://api-sandbox.pismolabs.io/corporate/earmarks \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --data '
{
     "from": {
          "account": {
               "id": "102701621"
          },
          "amount": 50,
          "currency": "USD"
     },
     "to": {
          "custom_info": {
               "type": "Scheduled earmark",
               "external_id": "123ABC"
          }
     },
     "tracking_id": "ABC123",
     "descriptor": "Hold Funds",
     "expiry_datetime": "2024-04-10T15:00:00Z"
}
'
```

For more information, refer to [Earmarks](https://developers.pismo.io/pismo-docs/docs/earmarks).

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v1/hierarchies` | `post-hierarchies` | Create hierarchy | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `POST /corporate/v2/divisions` | `post-division-v2` | Create division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` | `patch-division-v2` | Update division | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /corporate/v1/corporate-accounts` | `post-account` | Create transaction banking account | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /v1/accounts/{accountId}/flex-controls` | `post-v1-accounts-flex-controls` | Create account flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `GET /corporate/v1/corporate-accounts/{externalAccountId}` | `get-accounts` | Get transaction banking account information | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | Create earmark | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |
| `POST /corporate/v2/scheduled-payments` | `corporate-v2-post-scheduled-payments` | Schedule payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-02 |

### Operation essentials

- **`POST /corporate/v1/hierarchies`** (`post-hierarchies`): security `BearerAuth`; required parameters none declared; required body fields `name`, `levels`; response statuses 201, 400, 401, 403, 500; error codes in examples `WHIE0001`, `WHIE0002`, `WHIE0003`, `WHIE0004`, `WHIE0005`, `WHIE0007`, `ECMN9999`; events `corporate-hierarchy-creation-1`.
- **`POST /corporate/v2/divisions`** (`post-division-v2`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `hierarchy_id`, `level_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0017`, `WDIV0016`, `ECMN9999`; events `corporate-division-creation-2`.
- **`PATCH /corporate/v2/divisions/{divisionCode}`** (`patch-division-v2`): security `BearerAuth`; required parameters `divisionCode` (path); required body fields none declared; response statuses 204, 400, 401, 403, 404, 500; error codes in examples `WDIV0015`, `WDIV0011`, `WDIV0005`, `WDIV0007`, `WDIV0006`, `WDIV0008`, `WDIV0009`, `WDIV0010`, `WDIV0012`, `WDIV0018`, `WDIV0019`, `WDIV0002`, `WDIV0017`, `ECMN9999`; events `corporate-division-change-2`.
- **`POST /corporate/v1/corporate-accounts`** (`post-account`): security `BearerAuth`; required parameters none declared; required body fields `division_code`, `program_id`, `applicant`, `external_account_id`; response statuses 201, 400, 401, 403, 404, 409, 500; error codes in examples `WCAC0013`, `WCAC0005`, `WCAC0006`, `WCAC0004`, `WCAC0016`, `WCAC0009`, `WDIV0002`, `WCAC0011`, `WCAC0014`, `ECMN9999`; events `corporate-corporate-account-creation-1`, `onboarding-succeeded-1`.
- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /v1/accounts/{accountId}/flex-controls`** (`post-v1-accounts-flex-controls`): security `BearerAuth`; required parameters `accountId` (path); required body fields `type`, `name`, `deny_code`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL0701`, `RULVAL0400`, `ERUL0702`, `ERUL0703`, `ERUL0704`, `ERUL0706`, `ERUL0004`, `ERUL0002`, `RULVAL0403`, `WRUL0707`, `RULVAL0409`, `ERUL0001`, `RULREP0500`; events `audit-account-spending-limit-created-1`.
- **`GET /corporate/v1/corporate-accounts/{externalAccountId}`** (`get-accounts`): security `BearerAuth`; required parameters `externalAccountId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `WCAC0012`, `WDIV0002`, `WCAC0023`, `ECMN9999`; events none listed.
- **`POST /corporate/v2/earmarks`** (`post-corporate-v2-earmarks`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `internal_operation`; response statuses 201, 400, 401, 403, 409, 423, 500; error codes in examples `WOBK0007`, `WEAM0014`, `WEAM0015`, `WEAM0005`, `WEAM0006`, `WEAM0017`, `WEAM0019`, `WEAM0026`, `WEAM0036`, `WEAM0037`, `WEAM0039`, `WEAM0040`, `WEAM0047`, `WEAM0042`, `WEAM0043`, `WEAM0044`, `WEAM0045`, `WEAM0046`, `WEAM0016`, `WEAM0018`, `WEAM0009`, `WEAM0020`, `WEAM0023`, `WEAM0024`, `WEAM0001`, `WEAM0025`, `WEAM0034`, `WEAM0033`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `availables-change-available-1`, `corporate-earmark-1`, `platform-authorization-platform-authorization-1`, `transaction-creation-1`.
- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.
- **`POST /corporate/v2/scheduled-payments`** (`corporate-v2-post-scheduled-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`, `schedule_datetime`; response statuses 201, 400, 401, 403, 500; error codes in examples `WPMT0017`, `WPMT0018`, `WCMN0002`, `WCAC0010`, `WPMT0005`, `WPMT0006`, `WPMT0014`, `WPMT0053`, `WCAC0001`, `ECMN9999`; events `availables-change-available-1`, `corporate-schedule-payment-1`, `platform-authorization-platform-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `post-corporate-v2-earmarks` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `post-v1-accounts-flex-controls` | `audit-account-spending-limit-created-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `corporate-v2-post-scheduled-payments` | `availables-change-available-1` |
| `post-corporate-v2-earmarks` | `availables-change-available-1` |
| `post-account` | `corporate-corporate-account-creation-1` |
| `patch-division-v2` | `corporate-division-change-2` |
| `post-division-v2` | `corporate-division-creation-2` |
| `post-corporate-v2-earmarks` | `corporate-earmark-1` |
| `post-hierarchies` | `corporate-hierarchy-creation-1` |
| `corporate-v2-post-scheduled-payments` | `corporate-schedule-payment-1` |
| `post-account` | `onboarding-succeeded-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-scheduled-payments` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v2-earmarks` | `platform-authorization-platform-authorization-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |
| `post-corporate-v2-earmarks` | `transaction-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/corporate-banking-launch-reference.md`: updatedAt 2026-06-10T18:40:33.000Z.
- `docs/get-started/get-started-building-demand-deposit-accounts.md`: updatedAt 2026-06-29T19:37:33.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The grouped source pages have identical bodies (published twice under different URLs); both are kept verbatim for traceability.
- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/corporate-banking-launch-reference.md` | whole document | https://developers.pismo.io/pismo-docs/docs/corporate-banking-launch-reference | `7f3735781e85d6b8…` | 2026-06-10T18:40:33.000Z |
| `docs/get-started/get-started-building-demand-deposit-accounts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-building-demand-deposit-accounts | `097e956d81a53260…` | 2026-06-29T19:37:33.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-BANK-divisions-and-hierarchies` — Divisions and hierarchies
- `KU-BANK-earmarks` — Earmarks
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-audit` — Event catalogue: audit
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
- `KU-GS-setup-overview` — Core objects
- `KU-PAY-payments-configurations` — Payments configurations
