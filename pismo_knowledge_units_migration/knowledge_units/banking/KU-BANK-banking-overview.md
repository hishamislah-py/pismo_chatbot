---
ku_id: KU-BANK-banking-overview
title: Banking overview
category: banking
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/banking-overview.md
  sha256: f32f954ec9a7714a559140b49861e8ac3bcf027f984642a0058b3695886a2599
  url: https://developers.pismo.io/pismo-docs/docs/banking-overview
  role: primary_guide
  updated_at: '2026-06-25T17:27:44.000Z'
operations:
- delete-integrated-payments-api-v1-ebill-registration-accounts-accountId
- get-integrated-payments-api-v1-ebill-registration-accounts-accountId
- interest-bearing-calculate-average-balance
- interest-bearing-get-average-balance
- post-acquisitions-v3-s2s-applications
- post-create-fps
- post-integrated-payments-api-v1-bankslips-cashout
- post-integrated-payments-api-v1-bankslips-issue
- post-integrated-payments-api-v1-bankslips-pay
- post-integrated-payments-api-v1-ebill-registration-accounts-accountId
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban
- post-payments-v1-hold-funds-block
- post-pix-out-transfer
- post-save-provider-configuration
related_kus:
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--bank-slip-issuance
- KU-API-banking-integrated-payments--ebill-registration
- KU-API-banking-integrated-payments--transfer
- KU-API-banking-interest-bearing-accounts--average-balance
- KU-API-banking-ted-configuration--configurations
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-payment-methods--hold-funds
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-BANK-banking-as-a-service
- KU-BANK-how-overdraft-works
- KU-BANK-interest-bearing-accounts
- KU-BANK-transaction-banking-accounts
- KU-EVT-catalogue-account
- KU-EVT-catalogue-fps
- KU-EVT-catalogue-integrated
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-pix
- KU-PAY-bank-slips
- KU-PAY-faster-payment-system
- KU-PAY-hold-funds
- KU-PAY-pix-instant-payments
grouping_rationale: single source page
---

# Banking overview

**KU ID:** `KU-BANK-banking-overview` · **Category:** Banking · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/banking-overview.md`:

> Banking serves as the foundational back-end infrastructure responsible for processing daily banking transactions and maintaining up-to-date records of bank accounts and financial activities. It includes essential functionalities related to deposits and payments methods, while interfacing with general ledger systems and reporting tools.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/banking-overview.md`: Banking overview; On-demand banking; Alias bank; Banking as a Service (BaaS); Prospect management service; Banking providers; Bank account types; Bank account schemes; Interest-bearing accounts; Time deposit; Average balance calculation; Overdraft; Judicial block/unblock and transfer; Processing codes; Events; Instant payments; Wire transfers; National payment systems; Brazil; STR protocol; Bank slips; eBill; Brazil; Transaction banking

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 14 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/banking-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/banking-overview · updatedAt: 2026-06-25T17:27:44.000Z

<!-- source:begin path=docs/core-banking/banking-overview.md part=0-end -->

# Banking overview

Banking serves as the foundational back-end infrastructure responsible for processing daily banking transactions and maintaining up-to-date records of bank accounts and financial activities. It includes essential functionalities related to deposits and payments methods, while interfacing with general ledger systems and reporting tools.

Banking provides a unified banking experience for customers regardless of their geographic locations. This architecture aims to empower clients with enhanced independence, allowing them to manage their accounts and execute transactions from any location in the world. Read this guide to learn about Pismo’s banking products and gain insights into their features.

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Banking models</summary>

  ## On-demand banking

  On-demand banking represents a modern business model where banks or financial institutions leverage Pismo's banking technology to offer direct banking services to their customers. In this approach, financial entities streamline their operations, eliminating the reliance on third-party payment service providers for processing various payment types such as instant payments or bill payments. This grants financial institutions greater autonomy in managing and customizing their product offerings.\
  Typically, banks or financial institutions hold the operating license necessary to furnish on-demand banking services, thereby retaining full control over their service portfolio.

  ## Alias bank

  Alias bank is the business model for fintech companies authorized by the central bank to deliver banking services. While possessing a general operating license, they must  collaborate with providers to enable payment processing. Alias banks work in conjunction with both Pismo and partnering entities.

  For payment methods such as indirect instant payments and indirect wire transfers, clients are required to have their own operating license. Furthermore, lacking direct connectivity with the central bank, they must engage with a connectivity provider to deliver services. Examples of alias banks include:

  * Indirect wire transfers
  * Indirect instant payments
  * Bill payments

  ## Banking as a Service (BaaS)

  > 🚧 It's important to note that Pismo is a cloud-based technology platform and does not hold a charter or approval from the Central Bank of Brazil to directly provide banking or payment services. This responsibility belongs to our BaaS (Banking as a Service) partner providers, including BTG, Celcoin, Itaú, and JD Consultores. Pismo only provides the technology that enables our clients, in collaboration with our BaaS partners, to offer payment services.

  Banking as a Service (BaaS) is a business model where banks or other financial institutions extend their financial operations and infrastructure to serve non-financial client organizations (such as fintechs without a license, retailers, and utility companies). BaaS enables clients to embed financial products into their services without having to operate their own financial institutions and go through regulatory compliance.

  Generally, these companies offer financial services without holding a central bank license. Instead, they use the license of their Banking-as-a-Service (BaaS) provider who, in turn, assumes all regulatory responsibilities. Pismo streamlines the integration process with these providers, acting on behalf of the client.

  Pismo's BaaS model together with BaaS providers include:

  * Digital accounts
  * Wire transfers
  * Instant payments
  * Bill payments

  For more information, see [Banking as a Service](https://developers.pismo.io/pismo-docs/docs/banking-as-a-service)

  ### Prospect management service

  Pismo enables banks to automate the account opening, updating, and closing process. The journey starts when banks initiate prospect creation through the Acquisitions API ([Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)). From there, Pismo handles the orchestration by communicating with a banking provider to manage events, approve account creation, and validate or reject bank data.

  This asynchronous process offers significant advantages by eliminating the need for manual coordination between the banking provider and Pismo, allowing banks to focus on responding to events triggered by Pismo.

  > 📘 **Note**
  >
  > Pismo does not directly create bank accounts.

  Additionally, Pismo manages account updates and closures, serving as the orchestration layer between the bank and its underlying banking provider. For updates, banks can submit changes such as email, address, and phone number when using the Pismo's banking provider Celcoin, or update the account status when using Form3 (another Pismo banking provider). Pismo receives these requests and forwards them to the appropriate provider, ensuring data remains consistent across systems.

  For account closures, banks can set an account’s status to `CANCELLED` when working with Celcoin, or fully delete the bank account when integrated with Form3. In both scenarios, Pismo processes the closure request and executes the required action with the provider, ensuring the termination is correctly completed and reflected in the provider’s environment.

  Here are sample requests for creating bank accounts for individuals and businesses. For individual accounts, use [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) and complete the `personal` object within the `applicant` object. For business accounts, use the `company` object.

  <details>
    <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Individual account</summary>

    ```json
    {
      "application": {
        "submit": true,
        "prospect_cancel": false,
        "program_id": "program_id",
        "applicant": {
          "document_number": "document_number",
          "personal": {
            "name": "Jon Jones",
            "social_name": "Jon",
            "email": "jon.pay2all@email.com.br"
          },
          "birth_date": "03/03/1990",
          "addresses": [
            {
              "zip_code": "04514050",
              "address": "Address",
              "number": "100",
              "neighborhood": "Neighborhood",
              "complementary_address": "Suite 222",
              "city": "City",
              "state": "ST",
              "address_type": "RESIDENTIAL",
              "date": "17/09/2018",
              "mailing_address": true,
              "country": "Brasil",
              "phones": [
                {
                  "phone_type": "MOBILE",
                  "phone": "11991778123"
                }
              ]
            }
          ],
          "account": {
            "granted_limit": 1000,
            "password": "123456"
          }
        }
      }
    }
    ```
  </details>

  <details>
    <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Business  account</summary>

    ```json
     {
      "application": {
        "submit": false,
        "prospect_cancel": false,
        "program_id": "program_id",
        "applicant": {
          "document_number": "document_number",
        "company": {
            "external_id": "12345-EXT",
            "name": "Tech Solutions Ltd.",
            "email": "contact@techsolutions.com",
            "company_name": "Tech Solutions",
            "registration_number": "987654321",
            "activity": "Software Development",
            "company_type": "Private Limited",
            "company_format": "LLC",
            "company_constitution_date": "2010-05-15",
            "occupation": "Technology Services",
            "income": 5000000,
            "net_worth": 2000000,
            "annual_revenues": 60000000,
            "type": "Supplier",
            "number_of_partners": 3,
            "perc_ownership": 100,
            "fiscal_situation": "Active",
            "debt": 100000
        }
    },
          "birth_date": "03/03/1990",
          "addresses": [
            {
              "zip_code": "04514050",
              "address": "Address",
              "number": "100",
              "neighborhood": "Neighborhood",
              "complementary_address": "Suite 222",
              "city": "City",
              "state": "ST",
              "address_type": "RESIDENTIAL",
              "date": "17/09/2018",
              "mailing_address": true,
              "country": "Brasil",
              "phones": [
                {
                  "phone_type": "MOBILE",
                  "phone": "11991778123"
                }
              ]
            }
          ],
          "account": {
            "granted_limit": 1000,
            "password": "123456"
          }
        }
      }
    } 
    ```
  </details>

  ## Banking providers

  Pismo provides a comprehensive financial service structure through partnerships with central bank-licensed institutions (providers), enabling them to offer services for handling and moving funds. Additionally, for those with a central bank license seeking to expand their financial platform, Pismo facilitates this by connecting them with various providers.

  Pismo collaborates with many banking providers, including the following:

  <p>For BaaS:</p>

  <ul>
    <li>Celcoin</li>
    <li>Form3</li>
  </ul>

  <p>For Alias bank and On-demand banking:</p>

  <ul>
    <li>Celcoin</li>
    <li>IAAS (Itaú as a Service)</li>
    <li>BTG Pactual</li>
    <li>JD Consultores</li>
  </ul>
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Banking services</summary>

  ## Bank account types

  Pismo's platform provides versatile solutions for clients to establish various types of accounts across all business models, including On-demand, Alias bank, and Banking as a Service. Pismo’s microservices enable clients to configure different account types, catering to distinct use cases in a range of countries and regions. This adaptability ensures compliance with client requirements and regional regulations. Account options encompass current accounts, savings accounts, overdraft accounts, virtual accounts, and multi-currency accounts.

  ## Bank account schemes

  You can register global bank accounts with different identifying formats (schemes) for use on the Pismo platform with the [Bank accounts](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban) API. Among the options for registering bank accounts are schemes such as IBAN, BBAN, and schemes specific to a country or region. IBAN or International Bank Account Number (the most comprehensive account type) is a standard international numbering system used to identify an overseas bank account. The number starts with a two-digit country code, followed by two numbers and several more alphanumeric characters. IBAN does not replace a bank's own account numbering. Its only purpose is to provide additional information that helps identify overseas payments.

  ## Interest-bearing accounts

  Interest-bearing accounts are a type of bank account that allows clients to earn interest on deposited funds. The purpose of these bank accounts varies according to how clients use them; they can be used for short-term savings, emergency funds, specific goals such as travel or major purchases, or as part of a diversified investment strategy. Interest-bearing accounts provide a safer alternative to riskier investment options and offer a convenient solution for saving money while accruing interest. For more information, see [Interest-bearing accounts](https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts).

  ### Time deposit

  A time deposit account is a type of interest-bearing bank or credit union account that has a preset date of maturity. It requires bank customers to leave their money in the account for an agreed-upon length of time. If customers want to access the funds in a time deposit account, they must wait until the end of the term or risk having a penalty for early withdrawals. A certificate of deposit (CD) is the best-known example of time deposit accounts.

  Time deposits generally pay a slightly higher interest rate than a regular savings account. Usually the longer the time to maturity, the higher the interest payments.

  ### Average balance calculation

  This average is calculated using multiple closing balances over the selected period.

  Using [Calculate average balance](https://developers.pismo.io/pismo-docs/reference/interest-bearing-calculate-average-balance), you can specify a datetime range and calculate the average balance of an account over that period. This involves multiplying the balance by the number of days it has remained unchanged, summing the results, and then dividing them by the total number of days in the specified period. You can also retrieve an already calculate average for an account using [Get average balance](https://developers.pismo.io/pismo-docs/reference/interest-bearing-get-average-balance).

  ## Overdraft

  Overdraft is a financial service that lets you complete transactions even when your account balance is too low to cover them. It ensures that important payments and purchases can still go through during temporary cash shortfalls. By allowing transactions to proceed despite insufficient funds, an overdraft can help reduce potential disruptions and ease financial stress. For more information, refer to [How overdraft works](https://developers.pismo.io/pismo-docs/docs/how-overdraft-works).

  ## Judicial block/unblock and transfer

  Pismo partners with JD Consultores to automate judicial blocking and unblocking of account balances, including the transfer of previously blocked amounts. A judicial block is a temporary or permanent restriction placed on an account due to regulations, bank policies, or legal requirements. When applied, access to funds becomes limited, controlling when, how much, and by whom money can be withdrawn. The service supports both full and partial balance operations.

  Unlike the manual  [Hold funds](https://developers.pismo.io/pismo-docs/docs/hold-funds) feature, this automated service removes the need for clients to call the [Block amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block) API directly and provides a streamlined, hands‑off way to manage legally restricted funds.

  All communication and processing occur between Pismo and JD Consultores. Clients receive only the resulting events for block, unblock, and transfer actions.

  Upon receiving a judicial transfer instruction from the provider, the Pismo platform executes the cash‑out, and based on the completed transaction, generates the `STR0025` message. The Pismo platform then returns both the executed transfer order and the corresponding `STR0025` to the provider as confirmation that the transfer was successfully completed.

  The judicial block/unblock and transfer service works as follows.

  1. Client opens a configuration ticket with Pismo's banking team to request product setup.
  2. Pismo contacts the provider to coordinate the webhook configuration for you.
  3. The provider configures the required endpoints in your front‑end environment, known as the Command Cabin.
  4. Each day, the provider calls the Pismo endpoints to perform block, unblock, or transfer operations.
  5. When an operation occurs, the Pismo platform sends the corresponding event to you.

  ### Processing codes

  When the service is completed successfully, the Pismo platform returns the following processing codes to indicate the outcome.

  | Processing code | Description                        |
  | --------------- | ---------------------------------- |
  | `PSM016`        | Amount blocked                     |
  | `PSM017`        | Amount unblocked                   |
  | `PSM127`        | Blocked amount transferred         |
  | `PSM128`        | Reverse transferred blocked amount |

  ### Events

  The service generates these events.

  * For Account blocked/unblocked:
    * [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2)
  * For Amount blocked/unblocked/transferred:
    * [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)
    * [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1)
    * [Transfer-out created](https://developers.pismo.io/events/docs/integrated-payments-transfer-out-created-1)
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Payment and transfer services</summary>

  ## Instant payments

  Instant payments refer to digital payments that enable fund transfers in real time, 24 hours a day, 365 days a year, where the recipient can use the available funds immediately. Pismo supports two instant payment systems: Pix (Brazil) and Faster Payments (United Kingdom), and is developing integrations for other geographic locations.

  For more information, see:

  * [Pix instant payments (Brazil)](https://developers.pismo.io/pismo-docs/docs/pix-instant-payments)
  * [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer)
  * [Faster payments (UK)](https://developers.pismo.io/pismo-docs/docs/faster-payment-system)
  * [Send Faster payments](https://developers.pismo.io/pismo-docs/reference/post-create-fps)

  ## Wire transfers

  Wire transfers, electronic fund transfers between banks, are a service used by businesses and individuals alike. Pismo offers TED wire transfers within Brazil and is actively developing additional integration types. TED functions based on a client's setup with a provider authorized to perform TED transfers, thereby enabling clients to execute these transfers. Bank customers who initiate a TED transfer must use [Cash-out transfer](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-cashout).

  See [Register for TED transfers](https://developers.pismo.io/pismo-docs/reference/post-save-provider-configuration) for more details.

  ## National payment systems

  ### Brazil

  In Brazil, a national payment system such as SPB is a payment system that consists of entities, systems, and procedures governing the clearing and settlement of funds transfers, foreign currency operations, financial assets, and securities transactions. Its members are systems collectively known as Financial Market Infrastructure (FMI), which oversee a range of services, including:

  * Clearing and settlement of electronic debit and credit orders
  * Fund transfers
  * Settlement of securities transactions

  Under regulatory mandates, every financial institution (FI) and payment institution (PI) must establish an account with the central bank. These entities are legally obligated to monitor account transactions and report activities to the national financial system. As direct communication with the central bank is restricted, institutions must collaborate with Pismo to establish and use this service effectively.

  ### STR protocol

  To monitor account transactions, the Central Bank of Brazil (Bacen) uses the Sistema de Transferência de Reservas (STR), a real-time gross settlement system. Approved institutions use STR to format transactions into messages. Since financial and payment institutions cannot directly communicate with Bacen to generate STRs, they rely on Information Technology System Providers (PSTIs) to communicate with Bacen for generating STRs. In the Brazilian financial and payment system (SPB), transactions are irrevocable and processed individually. Pismo partners with JD Consultores to facilitate STR messaging, managing both [cash-out](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-cashout) transactions from Pismo accounts, and cash-in transactions from external accounts to Pismo accounts.

  STR is crucial for the stability and efficiency of the Brazilian financial system, providing a reliable infrastructure for the settlement of high-value transactions between financial institutions.

  To use the SPB product, the client must first contract with a PSTI such as JD Consultores, which  generates the necessary credentials and shares the endpoint URL with Pismo for message communication. Connectivity with Pismo must be established through either the public internet or privately through AWS Privatelink, and only institutions approved by Bacen are permitted to connect to the PSTI. Once connectivity is in place and the client's credentials are configured in Pismo, the client must select which messages to enable with Pismo. Pismo’s [cash-out](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-cashout) endpoint is available for transactional operations, and cash-in occurs automatically through communication between Pismo and the provider, ensuring that the client does not have to take any further action.

  Here is a list of the STR messaging codes. Each code corresponds to a specific transaction type or status update.

  | Code        | Description                                                                           |
  | ----------- | ------------------------------------------------------------------------------------- |
  | `STR0008`   | FI requests transfer between customer accounts                                        |
  | `STR0008R1` | Response to the transfer requester between customer accounts                          |
  | `STR0008R2` | Response to third parties regarding transfer between customer accounts                |
  | `STR0010`   | FI requests transfer for the refund of an incorrect transfer                          |
  | `STR0010R1` | Response to the transfer requester for the refund of an incorrect transfer            |
  | `STR0010R2` | Response to third parties regarding transfers for the refund of an incorrect transfer |
  | `STR0025`   | A judicial ordered transfer is executed                                               |
  | `STR0037R2` | Response to third parties regarding transfers that involve salary account             |
  | `STR0006R2` | Response to third parties regarding customer transfer to FI                           |
  | `STR0007R2` | Response to third parties regarding transfer from FI to customer account              |

  ## Bank slips

  Bank slips are used to pay bills, such as utilities, taxes, rent, and so on. In some countries, it is a common cash payment method. A bank slip is a bank voucher (printed or virtual) that can be paid to various financial institutions.

  Pismo offers [Issue bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-issue) and [Pay bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay) APIs, enabling you to generate and issue bank slips to your clients for payment and bank slip payments. Essentially, you use these APIs to create a bank slip and send it to Pismo's partner for processing. Consult the [Issue bank slips](https://developers.pismo.io/pismo-docs/docs/bank-slips#issue-bank-slips) section in *Bank slips* for more details.

  Here are the endpoints related to Pismo's bank slip feature:

  * [Bank slips](https://developers.pismo.io/pismo-docs/docs/bank-slips)
  * [Pay bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay)
  * [Issue bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-issue)

  > 📘 **Note**
  >
  > The returned line, due date, and amount reflect the officially registered bankslip and might differ from the values submitted. You should always use the returned information when processing payments.

  ## eBill

  ### Brazil

  In Brazil, DDA—**Débito Direto Autorizado**, commonly known as **Authorized Direct Debit**—provides an electronic view of bank slips linked to a specific document number (CPF or CNPJ), allowing for easier daily use without the need for paper documents. With DDA, you can pay bank slips directly through internet banking or a banking app, reducing the risk of errors associated with manually typing barcodes. Additionally, you can track all bank slips issued under your document number. It's important to note that non-bank charges, such as taxes and utility bills, are not processed via DDA.

  Only one active subscription or registration is permitted per account ID. Whenever a new bank slip (boleto) is issued to a document number subscribed to the DDA service, Pismo sends an event notification with the charge details, enabling you to pay the bill.

  Note that DDA does not automate payments. It merely provides an electronic view of the charge. The payer retains full control over when and how to complete the payment.

  > 📘 **About CPF and CNPJ**
  >
  > * CPF refers to the  Brazilian individual taxpayer registry identification which is required for individual and personal account types.
  > * CNPJ refers to the taxpayer identification number which is required for businesses and sole proprietorship accounts types.

  The Pismo platform provides an eBill API that enables you to use the DDA service.

  * **Register eBill**: Use the [Register eBill](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-ebill-registration-accounts-accountid) endpoint to register your document number (CPF/CNPJ) for DDA. This process is asynchronous as it relies on communication with service providers. You receive an [eBill registration status updated](https://developers.pismo.io/events/docs/integrated-payments-ebill-status-change-1) event notification when you have successfully registered your account using this endpoint.
  * **Get eBill registration**: Call [Get eBill registration](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-ebill-registration-accounts-accountid) to check the status of the DDA registration for a specific document number and determine if it is in `PROCESSING`, `ACTIVE`, or `INACTIVE` status.
  * **Delete eBill registration**: If you no longer wish to receive [notifications](https://developers.pismo.io/events/docs/banking-webhooks-ebill-notification-1) for charges associated with your document number, you can remove your registration using the [Delete eBill registration](https://developers.pismo.io/pismo-docs/reference/delete-integrated-payments-api-v1-ebill-registration-accounts-accountid) endpoint.

  > 📘 **Note**
  >
  > * Pismo provides the eBill feature in partnership with Celcoin and BTG. Partnerships with other providers are available upon request.
  > * DDA registration and deletion are processed only on weekdays, between 6 AM and 10 PM. If they are requested on a non-business day, the registration or deletion is scheduled for the next business day.
</details>

<details>
  <summary style={{ fontSize: "22px", fontWeight: "bold" }}>Transaction banking</summary>

  ## Transaction banking

  Transaction banking emphasizes precise management of both global and local operations. The goal is to create a clear view of the cashflow history and forecast for each account. Pismo offers a transaction banking solution founded on a distributed microservices architecture. This flexible design empowers you to selectively use the components that are relevant to your business application. As a result, you can develop a variety of products, from a simple ledger of virtual accounts to a sophisticated hierarchy of corporate accounts. These accounts can be organized under customized hierarchies and divisional structures. Moreover, Pismo's solution provides scheduled payment, file-based payment, earmarking, value dating, and other financial capabilities.

  For more information, see [Transaction banking](https://developers.pismo.io/pismo-docs/docs/corporate-banking-overview)
</details>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v2/accounts/{accountId}/bank-accounts/iban` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban` | Register IBAN account | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01 |
| `POST /v1/accounts/{accountId}/average-balance` | `interest-bearing-calculate-average-balance` | Calculate average balance | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--average-balance |
| `GET /v1/accounts/{accountId}/average-balance` | `interest-bearing-get-average-balance` | Get average balance | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--average-balance |
| `POST /payments/v1/payments/hold-funds/block` | `post-payments-v1-hold-funds-block` | Block amount | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01 |
| `POST /v1/payments/fps/out` | `post-create-fps` | Send Faster Payment [beta] | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | Perform cash-out | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--transfer |
| `POST /v1/provider-configuration` | `post-save-provider-configuration` | Register for TED transfers | `api-specs/Banking_-_TED_configuration.yaml` | no | KU-API-banking-ted-configuration--configurations |
| `POST /v1/bankslips-issue` | `post-integrated-payments-api-v1-bankslips-issue` | Issue bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | Pay bank slip | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `POST /v1/ebill-registration/accounts/{accountId}` | `post-integrated-payments-api-v1-ebill-registration-accounts-accountId` | Register eBill | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `GET /v1/ebill-registration/accounts/{accountId}` | `get-integrated-payments-api-v1-ebill-registration-accounts-accountId` | Get eBill registration | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `DELETE /v1/ebill-registration/accounts/{accountId}` | `delete-integrated-payments-api-v1-ebill-registration-accounts-accountId` | Delete eBill registration | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /v2/accounts/{accountId}/bank-accounts/iban`** (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `scheme`; response statuses 201, 400, 403, 404, 409, 500; error codes in examples `EIBA0009`, `EIBA0012`, `EIBA0006`, `EIBA0007`, `EIBA0023`, `EIBA0010`, `EIBA0028`, `EIBA0005`, `EIBA0011`, `EIBA0013`, `EIBA0015`; events `intl-bankaccounts-intl-bankaccount-register-1`.
- **`POST /v1/accounts/{accountId}/average-balance`** (`interest-bearing-calculate-average-balance`): security `BearerAuth`; required parameters `idempotency` (header), `accountId` (path); required body fields none declared; response statuses 202, 400, 404, 409, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0114`, `EIBACC0007`; events `average-balance-calculated-average-balance-1`.
- **`GET /v1/accounts/{accountId}/average-balance`** (`interest-bearing-get-average-balance`): security `BearerAuth`; required parameters `idempotency` (header), `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EIBACC0008`, `EIBACC0064`, `EIBACC0007`; events none listed.
- **`POST /payments/v1/payments/hold-funds/block`** (`post-payments-v1-hold-funds-block`): security `BearerAuth`; required parameters none declared; required body fields `tracking_id`, `account_id`, `amount`, `processing_code`; response statuses 201, 202, 400, 404, 500; error codes in examples `WP2P0000`; events `authorization-authorization-event-1`, `availables-change-available-1`.
- **`POST /pix/v1/pix/out/transfer`** (`post-pix-out-transfer`): security not declared; required parameters `Authorization` (header), `Idempotency-Key` (header); required body fields `account_id`, `amount`, `bank_account`, `initiation_type`, `ispb`, `payee`, `transaction_type`; response statuses 202, 400, 403, 404, 409, 429, 500, 502, 504; error codes in examples `EPIX0020`, `EPIX0032`, `EPIX0139`, `EPIX0132`, `EPIX0067`, `EPIX0126`, `EPIX0115`, `EPIX0226`, `EPIX0227`, `EPIX0228`, `EPIX0136`, `EPIX0022`, `EPIX0137`, `EPIX0138`, `EPIX0113`, `EPIX0123`, `EPIX0120`, `EPIX0124`, `EPIX0122`, `EPIX0141`, `EPIX0019`, `EPIX0008`, `EPIX0053`, `EPIX0003`, `EPIX0114`, `EPIX0061`, `EPIX0068`, `EPIX0130`, `EPIX0045`, `EPIX0110`, `EPIX0146`, `EPIX0160`, `EPIX0049`, `EPIX0009`, `EPIX0069`, `EPIX0010`, `EPIX0111`, `EPIX0112`, `EPIX0051`, `EPIX0041`, `EPIX0071`, `EPIX0142`, `EPIX0144`, `EPIX0085`, `EPIX0031`, `EPIX0004`, `EPIX0005`, `EPIX0007`, `EPIX0042`, `EPIX0017`, `EPIX0108`, `EPIX0109`, `EPIX0014`, `EPIX0043`, `EPIX0089`, `EPIX0046`, `EPIX0070`, `EPIX0018`, `EPIX0051`, `EPIX0060`, `EPIX0030`, `EPIX0050`, `EPIX0058`; events `pix-financial-reconciliation-1`, `pix-pix-in-1`, `pix-pix-out-1`.
- **`POST /v1/payments/fps/out`** (`post-create-fps`): security not declared; required parameters `Authorization` (header), `Idempotency-key` (header); required body fields `end_to_end_id`, `creditor_account`, `scheme_payment_type`, `currency`; response statuses 201, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EFPS0004`, `EFPS0016`, `EFPS0019`, `EFPS0025`, `EFPS0029`, `EFPS0037`, `EFPS0038`, `EFPS0039`, `EFPS0046`, `EFPS0047`, `EFPS0073`, `EFPS0002`, `EFPS0021`, `EFPS0033`, `EFPS0034`, `EFPS0035`, `EFPS0040`, `EFPS0041`, `EFPS0010`, `EFPS0018`, `EFPS0028`, `EFPS0031`, `EFPS0022`, `EFPS0036`, `EFPS0015`, `EFPS0006`, `EFPS0009`, `EFPS0011`, `EFPS0012`, `EFPS0017`, `EFPS0020`, `EFPS0023`, `EFPS0024`, `EFPS0026`, `EFPS0027`, `EFPS0030`, `EFPS0032`, `EFPS0014`; events `fps-fps-out-return-status-change-1`, `fps-fps-out-status-change-1`.
- **`POST /v1/transfers/cashout`** (`post-integrated-payments-api-v1-bankslips-cashout`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`, `processing_code`; response statuses 202, 400, 403, 409, 500, 502, 504; error codes in examples `EIP0003`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0016`, `EIP0017`, `EIP0020`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0029`, `EIP0030`, `EIP0031`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `integrated-payments-financial-reconciliation-1`, `integrated-payments-transaction-status-change-1`, `integrated-payments-transfer-out-created-1`.
- **`POST /v1/provider-configuration`** (`post-save-provider-configuration`): security `BearerAuth`; required parameters none declared; required body fields `branch`, `code`, `document_number`, `password`, `provider`, `url`, `user`; response statuses 201, 400, 403, 404, 500; error codes in examples `EBS0009`, `EBS0065`; events none listed.
- **`POST /v1/bankslips-issue`** (`post-integrated-payments-api-v1-bankslips-issue`): security `BearerAuth`; required parameters `x-idempotency-key` (header); required body fields `amount`, `due_date`; response statuses 202, 400, 403, 409, 500, 502; error codes in examples `EIP0010`, `EIP0012`, `EIP0013`, `EIP0016`, `EIP0017`, `EIP0023`, `EIP0077`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0029`, `EIP0042`, `EIP0065`, `EIP0015`, `EIP0014`, `EIP0007`, `EIP0004`, `EIP0011`, `EIP0028`, `EIP0022`, `EIP0070`, `EIP0074`, `EIP0018`, `EIP0024`; events `integrated-payments-bankslip-issue-register-1`.
- **`POST /v1/bankslips/pay`** (`post-integrated-payments-api-v1-bankslips-pay`): security `BearerAuth`; required parameters `Authorization` (header), `x-idempotency-key` (header); required body fields `account_id`, `amount`; response statuses 202, 400, 403, 404, 409, 500, 502, 504; error codes in examples `EIP0005`, `EIP0006`, `EIP0008`, `EIP0010`, `EIP0012`, `EIP0013`, `EIP0017`, `EIP0023`, `EIP0020`, `EIP0061`, `EIP0005`, `EIP0006`, `EIP0009`, `EIP0030`, `EIP0049`, `EIP0063`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0015`, `EIP0019`, `EIP0022`, `EIP0028`, `EIP0041`, `EIP0051`, `EIP0053`, `EIP0069`, `EIP0070`, `EIP0018`, `EIP0021`, `EIP0024`, `EIP0002`; events `authorization-authorization-event-1`, `integrated-payments-bankslip-status-change-1`, `integrated-payments-financial-reconciliation-1`.
- **`POST /v1/ebill-registration/accounts/{accountId}`** (`post-integrated-payments-api-v1-ebill-registration-accounts-accountId`): security `BearerAuth`; required parameters `accountId` (path), `x-idempotency-key` (header); required body fields none declared; response statuses 201, 400, 403, 409, 500, 502; error codes in examples `EIP0005`, `EIP0006`, `EIP0008`, `EIP0012`, `EIP0013`, `EIP0023`, `EIP0005`, `EIP0006`, `EIP0065`, `EIP0090`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0014`, `EIP0022`, `EIP0089`, `EIP0070`, `EIP0024`; events `integrated-payments-ebill-status-change-1`.
- **`GET /v1/ebill-registration/accounts/{accountId}`** (`get-integrated-payments-api-v1-ebill-registration-accounts-accountId`): security `BearerAuth`; required parameters `accountId` (path), `x-idempotency-key` (header); required body fields none declared; response statuses 200, 403, 404, 500; error codes in examples `EIP0005`, `EIP0006`, `EIP0088`, `EIP0007`, `EIP0089`; events none listed.
- **`DELETE /v1/ebill-registration/accounts/{accountId}`** (`delete-integrated-payments-api-v1-ebill-registration-accounts-accountId`): security `BearerAuth`; required parameters `accountId` (path), `x-idempotency-key` (header); required body fields none declared; response statuses 204, 400, 403, 404, 409, 500, 502; error codes in examples `EIP0012`, `EIP0013`, `EIP0023`, `EIP0091`, `EIP0005`, `EIP0006`, `EIP0088`, `EIP0062`, `EIP0065`, `EIP0004`, `EIP0007`, `EIP0011`, `EIP0014`, `EIP0022`, `EIP0089`, `EIP0070`, `EIP0024`; events `integrated-payments-ebill-status-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-integrated-payments-api-v1-bankslips-pay` | `authorization-authorization-event-1` |
| `post-payments-v1-hold-funds-block` | `authorization-authorization-event-1` |
| `post-payments-v1-hold-funds-block` | `availables-change-available-1` |
| `interest-bearing-calculate-average-balance` | `average-balance-calculated-average-balance-1` |
| `post-create-fps` | `fps-fps-out-return-status-change-1` |
| `post-create-fps` | `fps-fps-out-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-issue` | `integrated-payments-bankslip-issue-register-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-bankslip-status-change-1` |
| `delete-integrated-payments-api-v1-ebill-registration-accounts-accountId` | `integrated-payments-ebill-status-change-1` |
| `post-integrated-payments-api-v1-ebill-registration-accounts-accountId` | `integrated-payments-ebill-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-pay` | `integrated-payments-financial-reconciliation-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transaction-status-change-1` |
| `post-integrated-payments-api-v1-bankslips-cashout` | `integrated-payments-transfer-out-created-1` |
| `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban` | `intl-bankaccounts-intl-bankaccount-register-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |
| `post-pix-out-transfer` | `pix-financial-reconciliation-1` |
| `post-pix-out-transfer` | `pix-pix-in-1` |
| `post-pix-out-transfer` | `pix-pix-out-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `account-status-change-2` | account | 2 | https://developers.pismo.io/events/docs/account-status-change-2 | 6 | KU-EVT-catalogue-account |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `availables-change-available-1` | availables | 1 | https://developers.pismo.io/events/docs/availables-change-available-1 | 22 | KU-EVT-catalogue-other-domains |
| `integrated-payments-ebill-status-change-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-ebill-status-change-1 | 2 | KU-EVT-catalogue-integrated |
| `integrated-payments-transfer-out-created-1` | integrated | 1 | https://developers.pismo.io/events/docs/integrated-payments-transfer-out-created-1 | 1 | KU-EVT-catalogue-integrated |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/banking-overview.md`: updatedAt 2026-06-25T17:27:44.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 6 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/banking-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/banking-overview | `f32f954ec9a7714a…` | 2026-06-25T17:27:44.000Z |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--bank-slip-issuance` — API reference: Banking - Integrated payments — Bank slip issuance
- `KU-API-banking-integrated-payments--ebill-registration` — API reference: Banking - Integrated payments — eBill registration
- `KU-API-banking-integrated-payments--transfer` — API reference: Banking - Integrated payments — Transfer
- `KU-API-banking-interest-bearing-accounts--average-balance` — API reference: Banking - Interest-bearing accounts — Average balance
- `KU-API-banking-ted-configuration--configurations` — API reference: Banking - TED configuration — Configurations
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-payment-methods--hold-funds` — API reference: Core platform - Payment methods — Hold funds
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-BANK-how-overdraft-works` — How overdraft works
- `KU-BANK-interest-bearing-accounts` — Interest-bearing accounts
- `KU-BANK-transaction-banking-accounts` — Transaction banking and transaction banking accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-fps` — Event catalogue: fps
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-PAY-bank-slips` — Bank slips
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
- `KU-PAY-hold-funds` — Hold funds
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
