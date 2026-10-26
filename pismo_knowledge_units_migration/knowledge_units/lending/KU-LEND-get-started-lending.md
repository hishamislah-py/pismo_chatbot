---
ku_id: KU-LEND-get-started-lending
title: Get started with lending
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/get-started-with-lending.md
  sha256: 7b034b31557ae5c23f782f4db192593d263f5838bd69a5f6aee14f076cf74366
  url: https://developers.pismo.io/pismo-docs/docs/get-started-with-lending
  role: primary_guide
  updated_at: '2026-06-10T18:47:15.000Z'
- path: docs/get-started/get-started-building-lending.md
  sha256: 172c4311f2b2f4868b7293f4ed32604cddd4bad16a2db8a0cbfad6ebc0bf31df
  url: https://developers.pismo.io/pismo-docs/docs/get-started-building-lending
  role: primary_guide
  updated_at: '2026-06-29T19:37:33.000Z'
operations:
- CopyProgram
- CreateProgramBasedOnTemplate
- getProgramExportDownload
- postProgramExport
- postProgramImport
related_kus:
- KU-API-platform-setup-programs--export-and-import
- KU-API-platform-setup-programs--programs-part-01
- KU-CC-programs
- KU-CORE-accounting-overview
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-other-domains
- KU-GS-pismo-platform-onboarding
- KU-GS-program-types
- KU-LEND-lending-overview
- KU-LEND-loan-management
- KU-LEND-loan-products
grouping_rationale: Identical bodies (duplicate pages).
---

# Get started with lending

**KU ID:** `KU-LEND-get-started-lending` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Identical bodies (duplicate pages).

Scope as stated in `docs/lending/get-started-with-lending.md`:

> Use Pismo's lending solution to build loan products for your customers and to manage those loans throughout their lifecycle. Use this step-by-step guide to get started.

Scope as stated in `docs/get-started/get-started-building-lending.md`:

> Use Pismo's lending solution to build loan products for your customers and to manage those loans throughout their lifecycle. Use this step-by-step guide to get started.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/get-started-with-lending.md`: Get started with lending; Step 1: Create your organization (org); Step 2: Create programs; Step 3: Configure accounting; Step 4: Create loan products; Step 5: Book and manage loans
- `docs/get-started/get-started-building-lending.md`: Get started with lending; Step 1: Create your organization (org); Step 2: Create programs; Step 3: Configure accounting; Step 4: Create loan products; Step 5: Book and manage loans

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/get-started-with-lending.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-with-lending · updatedAt: 2026-06-10T18:47:15.000Z

<!-- source:begin path=docs/lending/get-started-with-lending.md part=0-end -->

# Get started with lending

Use Pismo's lending solution to build loan products for your customers and to manage those loans throughout their lifecycle. Use this step-by-step guide to get started.

For an overview of lending concepts, refer to [Lending overview](https://developers.pismo.io/pismo-docs/docs/lending-overview).

# Step 1: Create your organization (org)

An org is an object that represents your organization on the Pismo platform. Your Pismo support team creates your org. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 2: Create programs

Programs define the types of accounts a customer can open with your org, such as credit, debit, and lending accounts. You can't create customer accounts without at least one program, so you must complete this step.

There are three methods available for creating your program. You can use Control Center or APIs with each method.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Method
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Use a template
      </td>

      <td>
        Choose a program from one of our templates, enter the basic details about your program, and submit. We then create the program, and you can customize it when you’re ready.

        This method is the default.

        * **Control Center**—[Create a program from a template](https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template)
        * **APIs**—[Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate)
      </td>
    </tr>

    <tr>
      <td>
        Copy an existing program
      </td>

      <td>
        If you have existing programs, you can copy (or clone) a program and change some of the details. Be aware that you can’t change all the details.

        * **Control Center**—[Clone a program](https://developers.pismo.io/pismo-docs/docs/clone-a-program)
        * **APIs**—[Copy program](https://developers.pismo.io/pismo-docs/reference/copyprogram)
      </td>
    </tr>

    <tr>
      <td>
        Import a program
      </td>

      <td>
        You can use this method if you have programs in an existing test environment or another organization defined on the Pismo platform.

        * **Control Center**—[Export and import a program](https://developers.pismo.io/pismo-docs/docs/export-and-import-a-program)
        * **APIs:**\
          [Export program ](https://developers.pismo.io/pismo-docs/reference/postprogramexport)\
          [Download exported program](https://developers.pismo.io/pismo-docs/reference/getprogramexportdownload)\
          [Import program](https://developers.pismo.io/pismo-docs/reference/postprogramimport)
      </td>
    </tr>
  </tbody>
</Table>

If you're using the **Create program** endpoint, use the following fields. All fields are required. Fields for program setup that are not listed in this table are not applicable to lending.

| Field name              | Description                                                                | Field type | Possible values                                                                                                                                                                                  |
| :---------------------- | :------------------------------------------------------------------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                  | Name of the program                                                        | string     | Maximum length is 50 characters                                                                                                                                                                  |
| `type`                  | Type of program, which specifies the template that the Pismo platform uses | string     | Typical values for a lending program include `CURRENT ACCOUNTS`, `INTERNAL_ACCOUNTS`, `CORRESPONDENT ACCOUNTS`, and `LENDING`. For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types) |
| `timezone`              | Program time zone                                                          | string     | Internet Assigned Numbers Authority (IANA) time zone database "Region/City" format                                                                                                               |
| `currency_numeric_code` | Program ISO 4217 currency code                                             | string     | For example: 978 = Euro                                                                                                                                                                          |
| `country_code`          | ISO 3166 Alpha-3 program country code                                      | string     | For example: ESP = Spain                                                                                                                                                                         |

The following sample code shows how to use this endpoint to create a lending program named **Sample\_lending\_program**:

```curl
curl --request POST  
     --url <https://sandbox.pismolabs.io/programs/v1/programs/template>  
     --header 'Accept: application/json'  
     --header 'Authorization: Bearer <token value>'  
     --header 'Content-Type: application/json'  
     --data '  
{  
     "timezone": "America/Sao_Paulo",  
     "currency_numeric_code": "986",  
     "name": "Sample_lending_program",  
     "type": "LENDING"  
}'
```

<Callout icon="🚧" theme="warn">
  When you set up a program, you are prompted to accept default [processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types). If you choose not to accept them, then you must set up your own processing codes. If you don’t accept the default codes or set up your own, your disbursement and repayment requests will return errors.
</Callout>

# Step 3: Configure accounting

The Pismo platform provides tools to keep track of business and financial transactions for accounting purposes. It enables you to create general ledger accounts based on your organization's balance sheet. You can then configure accounting scripts that generate accounting entries based on accounting events.

For more information, refer to [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview).

# Step 4: Create loan products

Create loan products to match your lending business requirements. A loan product defines the options and rules individual loans inherit, including how often repayments are due, how interest is calculated, what limits apply, and so on. Loan products act as templates for your loans, so configuring them is a required first step before you can create any individual loan.

For more information, refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products).

# Step 5: Book and manage loans

With your loan products configured, you can now simulate, book, and disburse loans for your customers based on these products. You can also manage these loans at every stage, through settlement.

For more information, refer to [Manage loans](https://developers.pismo.io/pismo-docs/docs/manage-loans).

<br />

<br />

<br />
<!-- source:end -->

### Source 2: `docs/get-started/get-started-building-lending.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-building-lending · updatedAt: 2026-06-29T19:37:33.000Z

<!-- source:begin path=docs/get-started/get-started-building-lending.md part=0-end -->

# Get started with lending  

Use Pismo's lending solution to build loan products for your customers and to manage those loans throughout their lifecycle. Use this step-by-step guide to get started.

For an overview of lending concepts, refer to [Lending overview](https://developers.pismo.io/pismo-docs/docs/lending-overview).

# Step 1: Create your organization (org)

An org is an object that represents your organization on the Pismo platform. Your Pismo support team creates your org. For more information about org creation and all other onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Step 2: Create programs

Programs define the types of accounts a customer can open with your org, such as credit, debit, and lending accounts. You can't create customer accounts without at least one program, so you must complete this step.

There are three methods available for creating your program. You can use Control Center or APIs with each method.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Method
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Use a template
      </td>

      <td>
        Choose a program from one of our templates, enter the basic details about your program, and submit. We then create the program, and you can customize it when you’re ready.

        This method is the default.

        * **Control Center**—[Create a program from a template](https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template)
        * **APIs**—[Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate)
      </td>
    </tr>

    <tr>
      <td>
        Copy an existing program
      </td>

      <td>
        If you have existing programs, you can copy (or clone) a program and change some of the details. Be aware that you can’t change all the details.

        * **Control Center**—[Clone a program](https://developers.pismo.io/pismo-docs/docs/clone-a-program)
        * **APIs**—[Copy program](https://developers.pismo.io/pismo-docs/reference/copyprogram)
      </td>
    </tr>

    <tr>
      <td>
        Import a program
      </td>

      <td>
        You can use this method if you have programs in an existing test environment or another organization defined on the Pismo platform.

        * **Control Center**—[Export and import a program](https://developers.pismo.io/pismo-docs/docs/export-and-import-a-program)
        * **APIs:**\
          [Export program ](https://developers.pismo.io/pismo-docs/reference/postprogramexport)\
          [Download exported program](https://developers.pismo.io/pismo-docs/reference/getprogramexportdownload)\
          [Import program](https://developers.pismo.io/pismo-docs/reference/postprogramimport)
      </td>
    </tr>
  </tbody>
</Table>

If you're using the **Create program** endpoint, use the following fields. All fields are required. Fields for program setup that are not listed in this table are not applicable to lending.

| Field name              | Description                                                                | Field type | Possible values                                                                                                                                                                                  |
| :---------------------- | :------------------------------------------------------------------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                  | Name of the program                                                        | string     | Maximum length is 50 characters                                                                                                                                                                  |
| `type`                  | Type of program, which specifies the template that the Pismo platform uses | string     | Typical values for a lending program include `CURRENT ACCOUNTS`, `INTERNAL_ACCOUNTS`, `CORRESPONDENT ACCOUNTS`, and `LENDING`. For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types) |
| `timezone`              | Program time zone                                                          | string     | Internet Assigned Numbers Authority (IANA) time zone database "Region/City" format                                                                                                               |
| `currency_numeric_code` | Program ISO 4217 currency code                                             | string     | For example: 978 = Euro                                                                                                                                                                          |
| `country_code`          | ISO 3166 Alpha-3 program country code                                      | string     | For example: ESP = Spain                                                                                                                                                                         |

The following sample code shows how to use this endpoint to create a lending program named **Sample\_lending\_program**:

```curl
curl --request POST  
     --url <https://sandbox.pismolabs.io/programs/v1/programs/template>  
     --header 'Accept: application/json'  
     --header 'Authorization: Bearer <token value>'  
     --header 'Content-Type: application/json'  
     --data '  
{  
     "timezone": "America/Sao_Paulo",  
     "currency_numeric_code": "986",  
     "name": "Sample_lending_program",  
     "type": "LENDING"  
}'
```

<Callout icon="🚧" theme="warn">
  When you set up a program, you are prompted to accept default [processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types). If you choose not to accept them, then you must set up your own processing codes. If you don’t accept the default codes or set up your own, your disbursement and repayment requests will return errors.
</Callout>

# Step 3: Configure accounting

The Pismo platform provides tools to keep track of business and financial transactions for accounting purposes. It enables you to create general ledger accounts based on your organization's balance sheet. You can then configure accounting scripts that generate accounting entries based on accounting events.

For more information, refer to [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview).

# Step 4: Create loan products

Create loan products to match your lending business requirements. A loan product defines the options and rules individual loans inherit, including how often repayments are due, how interest is calculated, what limits apply, and so on. Loan products act as templates for your loans, so configuring them is a required first step before you can create any individual loan.

For more information, refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products).

# Step 5: Book and manage loans

With your loan products configured, you can now simulate, book, and disburse loans for your customers based on these products. You can also manage these loans at every stage, through settlement.

For more information, refer to [Manage loans](https://developers.pismo.io/pismo-docs/docs/manage-loans).

<br />

<br />

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /programs/v1/programs/copy` | `CopyProgram` | Copy program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /programs/v1/programs/export` | `postProgramExport` | Export program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--export-and-import |
| `GET /programs/v1/programs/export/{id}/download` | `getProgramExportDownload` | Download exported program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--export-and-import |
| `POST /programs/v1/programs/import` | `postProgramImport` | Import program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--export-and-import |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /programs/v1/programs/copy`** (`CopyProgram`): security `S2SAuthentication`; required parameters none declared; required body fields `base_program_id`, `name`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0064`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /programs/v1/programs/export`** (`postProgramExport`): security `S2SAuthentication`; required parameters none declared; required body fields `program_id`; response statuses 201, 400; error codes in examples none; events none listed.
- **`GET /programs/v1/programs/export/{id}/download`** (`getProgramExportDownload`): security `S2SAuthentication`; required parameters `id` (path); required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /programs/v1/programs/import`** (`postProgramImport`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `file`; response statuses 201, 400; error codes in examples none; events `programs-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CopyProgram` | `programs-creation-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |
| `postProgramImport` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/lending/get-started-with-lending.md`: updatedAt 2026-06-10T18:47:15.000Z.
- `docs/get-started/get-started-building-lending.md`: updatedAt 2026-06-29T19:37:33.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The grouped source pages have identical bodies (published twice under different URLs); both are kept verbatim for traceability.
- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/get-started-with-lending.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-with-lending | `7b034b31557ae5c2…` | 2026-06-10T18:47:15.000Z |
| `docs/get-started/get-started-building-lending.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-building-lending | `172c4311f2b2f486…` | 2026-06-29T19:37:33.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--export-and-import` — API reference: Platform setup - Programs — Export and import
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-CC-programs` — Control Center programs: create, edit, clone, export and import
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
- `KU-GS-program-types` — Program types
- `KU-LEND-lending-overview` — Lending overview and participants
- `KU-LEND-loan-management` — Loan management overview
- `KU-LEND-loan-products` — Loan products: overview and creation
