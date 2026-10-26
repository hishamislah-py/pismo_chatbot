---
ku_id: KU-RPT-brazilian-reports
title: Reports for Brazil
category: reports_and_data_files
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/brazilian-reports.md
  sha256: 81123b8d1a7ff501197e619e1249299072ef7bc2bbac4af4d7f4cdf8d9d8f2ba
  url: https://developers.pismo.io/pismo-docs/docs/brazilian-reports
  role: primary_guide
  updated_at: '2026-03-18T15:16:26.000Z'
operations: []
related_kus:
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Reports for Brazil

**KU ID:** `KU-RPT-brazilian-reports` · **Category:** Reports and data files · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/brazilian-reports.md`:

> These regulatory [scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports) are for Pismo customers that operate in Brazil.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/brazilian-reports.md`: Reports for Brazil

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/brazilian-reports.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/brazilian-reports · updatedAt: 2026-03-18T15:16:26.000Z

<!-- source:begin path=docs/data-and-reporting/brazilian-reports.md part=0-end -->

# Reports for Brazil

These regulatory [scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports) are for Pismo customers that operate in Brazil.

Information about regulatory requirements can be found at <a href="https://www.bcb.gov.br/estabilidadefinanceira/leiautedocumentoscrd" target="_blank">Leiaute de arquivos e base normativa</a> on the Central Bank of Brazil (BCB) website.

<HTMLBlock>
  {`
  <table border="0" cellpadding="0" cellspacing="0" width="1496" style="">
    <thead>
      <tr height="39" style="height: 29pt;">
        <th>Report&nbsp;</th>
        <th>Frequency&nbsp;</th>
        <th>Description&nbsp;</th>
        <th>Notes</th>
      </tr>
    </thead>

    <tbody>

  <!-- ACPO107 / ACPO111 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">ACPO107 / ACPO111&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Weekly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Positive Registry reports are used to create a database managed by specialized companies (database managers - GBDs) containing information provided by sources (banks, financial institutions, etc.) about the credits granted to their customers. The information that is within the scope of the Pismo platform is provided in two files:  
  ACPO107  –  Registration data provided by the participant (source)  
  ACPO111  –  Credit history provided by the participant (source)

  </br></br>Account and financial transaction databases are used to prepare the report.

  </br></br>For information about regulations, refer to the following websites.  
  </br>- <a href="https://www2.nuclea.com.br/SAP/Plano%20Homologat%C3%B3rio%20CPO%20-%20Novo%20Cadastro%20Positivo%20V1.2.0.pdf" target="_blank">Plano Homologatório do PCPO - Plataforma do Cadastro Positivo</a>  
  </br>- <a href="https://www2.nuclea.com.br/Compliance/MAPX-OP083-2019%20-%20Manual%20de%20Leiautes%20PCPO%20-%20Plataforma%20do%20Cadastro%20Positivo.pdf" target="_blank">Manual de Leiautes PCPO – Plataforma do Cadastro Positivo</a></td>

  <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
    <b>ACPO 107:</b></br></br>
  <b>Applies to:</b></br>
  FULL BALANCE</br></br>
  <b>Delivery format options:</b></br>
  XML (BCB - Brazil)</br>
  Parquet (Pismo clients)</br></br>
  <b>Granularity of information:</b></br>
    Account</br></br>
  <b>ACPO 111:</b></br></br>
  <b>Applies to:</b></br>
  FULL BALANCE</br></br>
  <b>Delivery format options:</b></br>
  XML (BCB - Brazil)</br>
  Parquet (Pismo clients)</br></br>
  <b>Granularity of information:</b></br>
  Account
  </td>

  </tr>

  <!-- Annual Fee Report -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Annual Fee Report&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Annually&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The annual fee statement is a consolidated document that details, month by month, the amounts charged during the previous year in fees, interest, late payment charges, fines, and other expenses related to credit or leasing operations. It allows the customer to simply and easily track how much they spent on these fees.

  </br></br>Financial transaction databases are used to prepare the report.

  For information about regulations, refer to <a href="https://normativos.bcb.gov.br/Lists/Normativos/Attachments/49514/Res_3919_v1_O.pdf" target="_blank">RESOLUÇÃO Nº 3.919</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  PRE-PAID</br>
  FULL BALANCE</br></br>
  <b>Delivery format options:</b></br>
  Parquet (Pismo clients)</br>
  CSV (BCB - Brazil)</br>
  JSON (BCB - Brazil)</br></br>
  <b>Granularity of information:</b></br>
  Organization
  </td>

  <!-- APIX 001 - 1201 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">APIX 001 - 1201&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">APIX001 is a file in XML format that contains detailed information about transactions carried out via Pix by a financial institution.

  </br></br>Investments and financial transaction databases are used to prepare the report.

  </br></br>For regulatory information, download this <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Remessa_informacoes_Pix/APIX001_2-4.xlsx">spreadsheet</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  PRE-PAID</br></br>

  <b>Delivery format options:</b></br>
  XML (BCB - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Organization 
  </td>

  </tr>

  <!-- CADOC-3040 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">CADOC-3040&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The CADOC 3040 report is of an individual nature and must be sent monthly to each financial institution. It provides information about credit operations in the portfolios of its supervised entities.

  </br></br>Financial transaction databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.bcb.gov.br/estabilidadefinanceira/scrdoc3040" target="_blank">Documento 3040 e Documento 3026</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  XML (BACEN - Brazil)</br>
  Parquet (Pismo clients)</br></br>

  <b>Granularity of information:</b></br>
  Account</br>
  Document number (CPF or CNPJ)
  </td>

  </tr>

  <!-- CADOC-3050 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">CADOC-3050&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Daily (Parquet) or Weekly (XML)&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">CADOC-3050, also known as “Average Rates”,  is a report established by the Central Bank  that aims to systematically obtain the average rates charged by financial institutions in the various types of credit available on the market, which allows the final borrower to have, through the BACEN itself, a comparative basis of contracting rates before even contracting credit operations.

  </br></br>Financial transaction databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=335" target="_blank">Documento 3050</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  XML (BCB - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Account</br>
  Document number (CPF or CNPJ)
  </td>

  </tr>

  <!-- CADOC-5816 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">CADOC-5816&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">International reports. Contains cross-border network transactions.

  Financial transaction databases are used to prepare the report.

  For information about regulations, refer to <a href="https://www.bcb.gov.br/estabilidadefinanceira/leiautedocumento5816" target="_blank">Leiaute do documento 5816</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  PRE-PAID</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  Positional TXT (BCB - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Document number (CPF/CNPJ)
  </td>

  </tr>

  <!-- CADOC-6209 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">CADOC-6209&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Quarterly (Trimester)&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Contains information about retail payments and service channels.

  </br></br>Accounting databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=335" target="_blank">this document</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  FULL BALANCE</br></br>

  <b>Delivery format ons:</b></br>
  Positional TXT (BCB - Brazil)</br>
  Parquet (Pismo clients)</br></br>

  <b>Granularity of information:</b></br>
  Organization
  </td>

  </tr>

  <!-- CADOC-6308 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">CADOC-6308&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Contains data on card operation, such as the number of cards issued, the financial amount transacted, and so on.

  </br></br>Accounting databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/arranjos/Elabora%C3%A7%C3%A3o%20e%20Remessa%20de%20Informa%C3%A7%C3%B5es%20Relativas%20aos%20Cart%C3%B5es%20de%20Pagamento%20%20Emissores%20-%20Doc%206308.pdf" target="_blank">this document</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  Positional TXT (BCB - Brazil)</br>
  Parquet (Pismo clients)</br></br>

  <b>Granularity of information:</b></br>
  Organization
  </td>

  </tr>

  <!-- CCS -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">CCS&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Daily&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">This is the same as the Client Base Report CCS - ACCS001, except that, instead of consisting of one XML file, it consists of two CSV files in the format expected by JD.

  </br></br>(JD is a company that provides a link between some financial institutions and regulatory agencies. Financial institutions that use JD must provide the CSS report in the format expected by JD.)

  </br></br>Account databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.jdconsultores.com.br/regulatorios/" target="_blank">this JD document</a>.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  PRE-PAID</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  XML (BACEN - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Document number (CPF/CNPJ)
  </td>

  </tr>

  <!-- CCS - JD CABINE CCS -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">CCS - JD CABINE CCS&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">This is the same as the Client Base Report CCS - ACCS001, except that, instead of consisting of one XML file, it consists of two CSV files in the format expected by JD.

  </br></br>(JD is a company that provides a link between some financial institutions and regulatory agencies. Financial institutions that use JD must provide the CSS report in the format expected by JD.)

  </br></br>Account databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.jdconsultores.com.br/regulatorios/" target="_blank">this JD document</a>.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  PRE-PAID</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  TXT (JD Format)</br></br>

  <b>Granularity of information:</b></br>
  Document number (CPF/CNPJ) 
  </td>

  </tr>

  <!-- COSIF 4010 / 4016 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">COSIF 4010 / 4016&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly / Bi-annual (Semester)&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Documents 4010 and 4016 contain accounting information relating to the Trial Balance and Analytical Balance Sheet, respectively, as defined in COSIF – Accounting Standard for Institutions Regulated by the Central Bank of Brazil.

  </br></br>Accounting databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.bcb.gov.br/estabilidadefinanceira/leiautescosif" target="_blank">Leiautes dos documentos do Sistema Cosif</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  PRE-PAID</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b> </br>
  XML (BCB - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Account</br></br>
  </td>

  </tr>

  <!-- COSIF 4111 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">COSIF 4111&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Daily&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Document 4111 is intended for the submission of daily information on accounting balances of an asset, liability, or compensation nature.

  </br></br>Accounting databases are used to prepare the report.

  </br></br>For information about regulations, refer to <a href="https://www.bcb.gov.br/estabilidadefinanceira/leiautescosif" target="_blank">Leiautes dos documentos do Sistema Cosif</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  PRE-PAID</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  XML (BCB - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Account
  </td>

  </tr>

  <!-- DECRED -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">DECRED&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Bi-annual (Semester)&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Contains transactions made with credit cards, including the identification of the users of the credit card services and the global amounts handled monthly. The Federal Revenue Service uses the information in this report to cross-check taxpayers, and if the value of sales reported by the administrators is higher than the company's revenue reported in the income statement, the difference is taxed with a fine and interest.

  </br></br>Financial transaction databases are used to prepare the report.

  </br></br>For information about regulations, refer to the following website.</br>
  <a href="https://www.normaslegais.com.br/legislacao/instrucao-normativa-srf-341-2003.htm" target="_blank">INSTRUÇÃO NORMATIVA SRF Nº 341\\</a></td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  Positional TXT (BCB - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Month</br>
  Statement</br>
  Document number (CPF/CNPJ)</br>
  </td>

  </tr>

  <!-- DIMP -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">DIMP&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">DIMP (Declaration of Payment Method Reports) provides information related to transactions with debit, credit, store (private label) cards and other electronic payment instruments. On-us transactions are included, since the customer, as the person responsible for capturing the transactions, has the responsibility to report them. Off-us transactions are not included.

  </br></br>Financial transaction databases are used to prepare the report.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  MERCHANTS</br></br>

  <b>Delivery format options:</b></br>
  TXT separated by pipes (BCB - Brazil)</br>
  Parquet (Pismo clients)</br></br>

  <b>Granularity of information:</b></br>
  Organization
  </td>

  </tr>

  <!-- E-financial -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">E-financial&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly or Bi-annual (Semester)&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">This is an obligation that gathers various information related to financial transactions of interest to the Brazilian Federal Revenue Service (RFB). It consists of a set of files to be delivered in specific layouts, specified by the Public Digital Bookkeeping System (SPED), in order to provide information about the balances, income, and investments of customers' checking and savings accounts, as well as other information regarding their transactions.

  </br></br>Investments and financial transaction databases are used to prepare the report.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  CORE BANKING and INTEREST MANAGEMENT</br></br>

  <b>Delivery format options:</b></br>
  XML (RFB - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Account</br>
  Document number (CPF/CNPJ)
  </td>

  </tr>

  <!-- FGC -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">FGC&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">The Credit Guarantee Fund (FGC) is part of the protection network of the National Financial System. It acts to protect depositors and investors through the payment of guarantees, in cases of intervention or liquidation of an associated financial institution, and might also provide support to associated financial institutions, including liquidity operations.

  </br></br>Financial transaction databases are used to prepare the report.

  </br></br>For information about regulations, refer to the following websites.</br>
  - <a href="https://www.bcb.gov.br/en/financialstability/FGC_and_FGCoop" target="_blank">Deposit insurance (FGC and FGCoop)</a></br>
  - <a href="https://www.bcb.gov.br/htms/normativ/Circular3915.pdf?r=1" target="_blank">CIRCULAR Nº 3.915, DE 17 DE OUTUBRO DE 2018\\</a></td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br> 
  ASSETS</br>
  INTEREST MANAGEMENT</br></br>

  <b>Delivery format options:</b></br>
  JSON (BACEN - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Document number (CPF/CNPJ)
  </td>

  </tr>

  <!-- SVR 9800 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">SVR 9800&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Contains information about funds, such as closed account balances, that the institution needs to refund.

  </br></br>Account and financial transaction databases are used to prepare the report.

  </br></br>For information about regulations, download this <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/Leiaute_de_documentos/arquivos_xsd.zip">spreadsheet</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  CSV (BCB - Brazil)</br>
  XML (JD - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Document number (CPF/CNPJ)
  </td>

  </tr>

  <!-- SVR 9805 -->
      <tr height="225" style="height: 169pt;">

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">SVR 9805&nbsp;</td>

        <td height="225" class="xl69" width="130" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt; border-style: solid; border-color: black windowtext windowtext; border-image: initial; height: 169pt; width: 125pt;">Monthly&nbsp;</td>

        <td class="xl70" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 291pt;">Contains information about amounts refunded to individuals and legal entities.

  </br></br>Account and financial transaction databases are used to prepare the report.

  </br></br>For information about regulations, download this <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/Leiaute_de_documentos/arquivos_xsd.zip">spreadsheet</a> from the BCB.</td>

       <td class="xl87" width="400" style="padding-top: 1px; padding-right: 1px; padding-left: 6px; color: black; vertical-align: middle; border-width: 0.5pt 1pt 1pt 0.5pt; border-style: solid; border-color: black windowtext windowtext black; border-image: initial; width: 212pt;">
  <b>Applies to:</b></br>
  DEBIT</br>
  FULL BALANCE</br></br>

  <b>Delivery format options:</b></br>
  CSV (BCB - Brazil)</br>
  XML (JD - Brazil)</br></br>

  <b>Granularity of information:</b></br>
  Document number (CPF/CNPJ)
  </td>

  </tr>

    </tbody>
  </table>    
  `}
</HTMLBlock>
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/brazilian-reports.md`: updatedAt 2026-03-18T15:16:26.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/brazilian-reports.md` | whole document | https://developers.pismo.io/pismo-docs/docs/brazilian-reports | `81123b8d1a7ff501…` | 2026-03-18T15:16:26.000Z |

## Related knowledge units

- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
