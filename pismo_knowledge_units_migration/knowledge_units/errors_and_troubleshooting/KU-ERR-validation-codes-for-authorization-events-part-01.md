---
ku_id: KU-ERR-validation-codes-for-authorization-events-part-01
title: Validation codes for authorization events (part 1 of 2)
category: errors_and_troubleshooting
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/validation-codes-for-authorization-events.md
  sha256: dc858d8fce83262803a23526de2e278b406eb9f115cb773be4f5a399212d7858
  url: https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events
  role: primary_guide
  updated_at: '2026-08-06T02:48:36.000Z'
operations: []
related_kus:
- KU-ERR-validation-code-definitions
grouping_rationale: single source page; split into parts because the page is very large
---

# Validation codes for authorization events (part 1 of 2)

**KU ID:** `KU-ERR-validation-codes-for-authorization-events-part-01` · **Category:** Errors and troubleshooting · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/validation-codes-for-authorization-events.md`:

> An authorization event uses a validation code to indicate what type of action generated it. You can find the card network's validation code in the `response_code` field.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/validation-codes-for-authorization-events.md`: Validation codes for authorization events; Authorization validations

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/validation-codes-for-authorization-events.md` lines 1–3005 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events · updatedAt: 2026-08-06T02:48:36.000Z

<!-- source:begin path=docs/card-issuing/validation-codes-for-authorization-events.md part=0-3005 -->

# Validation codes for authorization events

An authorization event uses a validation code to indicate what type of action generated it. You can find the card network's validation code in the `response_code` field.

If a validation fails, the Pismo platform uses a custom validation code to provide more specific reasons for why it failed. You can find the custom code for an event in the `denial_code` field.

An authorization event falls into one of two categories: **stateless** or **stateful**.

A stateless event is independent of other events. For example, if an event indicates that an invalid expiration date was provided, then the transaction is over. Of course, the card holder can enter the correct expiration date, but when they submit the new data, a new transaction is generated – a transaction that is completely independent of the old transaction. So "Invalid expiration date provided" is a stateless event.

On the other hand, if a card holder reports a card as stolen, the platform generates a "Card status ROBBED or THEFT" event. The platform needs to do more processing after issuing this event – to block the card, for example. Since this is an on-going transaction, it's a stateful event.

The following tables list all the custom codes that the Pismo platform uses for authorization events. An event only contains one of these codes if validation fails. Approved transactions don't have custom codes.

# Authorization validations

**KEY**:\
**CC** = Custom code, **SL** = Stateless, **SF** = Stateful, **ZBV** = Zero balance validation, **Merch DC** = Merchant Denial Code, **VDC** = Visa denial code, **MDC** = Mastercard denial code, **TDC** = TecBan denial code, **RDC** = RuPay denial code, **EDC** = ELO denial code, **CD** = Customer decides

<Table align={["left","left","left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        CC
      </th>

      <th style={{ textAlign: "left" }}>
        Name
      </th>

      <th style={{ textAlign: "left" }}>
        State
      </th>

      <th style={{ textAlign: "left" }}>
        ZBV
      </th>

      <th style={{ textAlign: "left" }}>
        Merch

        DC
      </th>

      <th style={{ textAlign: "left" }}>
        VDC
      </th>

      <th style={{ textAlign: "left" }}>
        MDC
      </th>

      <th style={{ textAlign: "left" }}>
        TDC
      </th>

      <th style={{ textAlign: "left" }}>
        RDC
      </th>

      <th style={{ textAlign: "left" }}>
        EDC
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        [91](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#91---authorization-system-or-issuer-system-inoperative)
      </td>

      <td style={{ textAlign: "left" }}>
        Authorization system or issuer system inoperative
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        91
      </td>

      <td style={{ textAlign: "left" }}>
        91
      </td>

      <td style={{ textAlign: "left" }}>
        91
      </td>

      <td style={{ textAlign: "left" }}>
        91
      </td>

      <td style={{ textAlign: "left" }}>
        91
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [810](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#810---available-limit-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        Available insufficient balance validation
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        51
      </td>

      <td style={{ textAlign: "left" }}>
        51
      </td>

      <td style={{ textAlign: "left" }}>
        51
      </td>

      <td style={{ textAlign: "left" }}>
        51
      </td>

      <td style={{ textAlign: "left" }}>
        51
      </td>

      <td style={{ textAlign: "left" }}>
        51
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [810](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#810---available-limit-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        Available withdrawal limit validation
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        61
      </td>

      <td style={{ textAlign: "left" }}>
        61
      </td>

      <td style={{ textAlign: "left" }}>
        61
      </td>

      <td style={{ textAlign: "left" }}>
        61
      </td>

      <td style={{ textAlign: "left" }}>
        61
      </td>

      <td style={{ textAlign: "left" }}>
        51
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [998](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#998---card-hash-not-present-in-the-database)
      </td>

      <td style={{ textAlign: "left" }}>
        Card hash not present in database
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        56
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [ACE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ace---network-transactions-api-communication-error)
      </td>

      <td style={{ textAlign: "left" }}>
        network-transactions-api communication error
      </td>

      <td style={{ textAlign: "left" }}>
        Both
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [ACT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#act---a-timeout-occurred-while-fetching-account)
      </td>

      <td style={{ textAlign: "left" }}>
        Account timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [AEE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#aee---anti-fraud-external-generic-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Anti-fraud external generic error
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [AET](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#aet---anti-fraud-external-api-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Anti-fraud external API timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [AFE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#afe---anti-fraud-internal-generic-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Anti-fraud internal API generic error
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [AGE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#age---unexpected-error-while-fetching-account)
      </td>

      <td style={{ textAlign: "left" }}>
        Account generic error
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [AIT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ait---anti-fraud-internal-api-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Anti-fraud internal API timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [ANF](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#anf---acceptance-not-found)
      </td>

      <td style={{ textAlign: "left" }}>
        Acceptance not found
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        03
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [AUD](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#aud---authorization-disabled)
      </td>

      <td style={{ textAlign: "left" }}>
        Authorization disabled
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        78
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        78
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [BCE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#bce---balance-config-generic-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Balance Config generic error
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [BCT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#bct---balance-config-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Balance Config timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [BII](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions-copy#bii---balance-inquiry-internal-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Balance inquiry internal error
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CAT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cat---config-api-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Config API timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CAV](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cav---cavv-3ds-validation-result)
      </td>

      <td style={{ textAlign: "left" }}>
        CAVV - 3DS VALIDATION
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        12
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CED](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ced---invalid-expiration-date-provided)
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid expiration date provided
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CET](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cet---card-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Card timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CGE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cge---card-generic-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Card generic error
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CLF](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#clf---credit-limit-impact-not-found)
      </td>

      <td style={{ textAlign: "left" }}>
        Credit limit impact not found
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CMD](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cmd---card-mode-disabled)
      </td>

      <td style={{ textAlign: "left" }}>
        Card mode disabled
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57\
        (invalid mode)

        AB\
        (debit)

        AC\
        (credit)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CNC](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cnc---account-cancelled)
      </td>

      <td style={{ textAlign: "left" }}>
        Account cancelled
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        46
      </td>

      <td style={{ textAlign: "left" }}>
        62
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        46
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CND](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cnd---account-blocked)
      </td>

      <td style={{ textAlign: "left" }}>
        Account blocked
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        62
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        62
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CNU](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cnu---account-status-unknown)
      </td>

      <td style={{ textAlign: "left" }}>
        Account status unknown
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        62
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CTE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cte---transaction-counter-exceeded)
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction counter exceeded
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        54
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CTT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ctt---card-token-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Card token timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [CV3](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#cv3---cvc3-not-configured)
      </td>

      <td style={{ textAlign: "left" }}>
        CVC3 not configured
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [DCC](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#dcc---dcc-transaction-not-allowed-for-program)
      </td>

      <td style={{ textAlign: "left" }}>
        DCC transaction not allowed for program
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [DCE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#dce---distributor-api-communication-error)
      </td>

      <td style={{ textAlign: "left" }}>
        distributor-api communication error
      </td>

      <td style={{ textAlign: "left" }}>
        Both
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [DCM](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#dcm---original-authorization-not-found-at-refund)
      </td>

      <td style={{ textAlign: "left" }}>
        Original authorization not found at refund
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        12
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        12
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        12
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [DIC](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#dic---invalid-country-for-dcc-definition)
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid country for DCC definition
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [DIY](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#diy---invalid-currency-for-dcc-definition)
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid currency for DCC definition
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [ETR](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#etr---exceed-time-to-reversal)
      </td>

      <td style={{ textAlign: "left" }}>
        Exceed time to reversal
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        12
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FAT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fat---atc-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        ATC validation
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        01
      </td>

      <td style={{ textAlign: "left" }}>
        05
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FL6](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fl6---card-blocked-by-anti-fraud)
      </td>

      <td style={{ textAlign: "left" }}>
        Card blocked by anti-fraud
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        59
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FR1](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fr1-and-fr2---cvvcvc-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        CVV1 or CVC1 validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        05
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FR2](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fr1-and-fr2---cvvcvc-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        CVV2 or CVC2 validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N7
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        05
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FR3](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fr3---iav----intelligent-account-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        IAV validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FR5](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fr5---transaction-made-with-magnetic-stripe-in-a-country-where-its-not-allowed-to-be-used)
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction made with magnetic stripe in a country where it's not allowed to be used
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        R9
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FR6](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fr6---password-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        Password validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        55
      </td>

      <td style={{ textAlign: "left" }}>
        55
      </td>

      <td style={{ textAlign: "left" }}>
        55
      </td>

      <td style={{ textAlign: "left" }}>
        55
      </td>

      <td style={{ textAlign: "left" }}>
        55
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FR7](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fr7---card-not-present-in-database)
      </td>

      <td style={{ textAlign: "left" }}>
        Card not present in database
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FRE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fre---cryptogram-data-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        Cryptogram data validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        R9
      </td>

      <td style={{ textAlign: "left" }}>
        E3
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FRH](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#frh---pos-point-of-sale-entry-mode-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        POS (Point-of-Sale) entry mode validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        58
      </td>

      <td style={{ textAlign: "left" }}>
        58
      </td>

      <td style={{ textAlign: "left" }}>
        58
      </td>

      <td style={{ textAlign: "left" }}>
        58
      </td>

      <td style={{ textAlign: "left" }}>
        58
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FRN](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#frn---chip-field-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        Chip field validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        R9
      </td>

      <td style={{ textAlign: "left" }}>
        E3
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [FRO](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#fro---chip-signature-validation)
      </td>

      <td style={{ textAlign: "left" }}>
        Chip signature validation
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>

      <td style={{ textAlign: "left" }}>
        88
      </td>

      <td style={{ textAlign: "left" }}>
        R9
      </td>

      <td style={{ textAlign: "left" }}>
        81
      </td>

      <td style={{ textAlign: "left" }}>
        82
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [GCD](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#gcd---gcd-gift-card-denial)
      </td>

      <td style={{ textAlign: "left" }}>
        Gift card denial
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [HCE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#hce---hsm-communication-error)
      </td>

      <td style={{ textAlign: "left" }}>
        HSM communication error
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [IAT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#iat---invalid-account-type)
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid account type
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        AB\
        (debit)

        AC (credit)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [IMA](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ima---invalid-message-authentication-code)
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid message authentication code (MAC)
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        89
      </td>

      <td style={{ textAlign: "left" }}>
        63
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [IMF](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#imf---invalid-message-format)
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid message format
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        12 or 5C
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [ISE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ise---insufficient-statements)
      </td>

      <td style={{ textAlign: "left" }}>
        Insufficient statements
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [IZA](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions-copy#iza---zero-amount-not-allowed)
      </td>

      <td style={{ textAlign: "left" }}>
        Zero amount not allowed
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        13
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [LAE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#lae---an-unexpected-error-happened-while-getting-the-account-information)
      </td>

      <td style={{ textAlign: "left" }}>
        An unexpected error happened while fetching the account information
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [LCT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#lct---ledger-account-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Ledger account timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [LNF](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#lnf---account-not-found)
      </td>

      <td style={{ textAlign: "left" }}>
        Account not found
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        56
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        14
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [LUD](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#lud---limit-update-duplicated-id-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Limit update duplicated ID error
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [LUE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#lue---error-on-update-ledger)
      </td>

      <td style={{ textAlign: "left" }}>
        Error on update Ledger
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [LUT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#lut---ledger-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Ledger timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [MDC](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#mdc---multi-currency-not-allowed-for-dcc-authorization)
      </td>

      <td style={{ textAlign: "left" }}>
        Multi-currency not allowed for DCC authorization
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        5X
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [MPC](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#mpc---program-config-not-found)
      </td>

      <td style={{ textAlign: "left" }}>
        Program config not found
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [NCV](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ncv---entry-mode-not-allowed-with-no-cvm)
      </td>

      <td style={{ textAlign: "left" }}>
        Entry mode not allowed with no-CVM
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [OON](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#oon---org-operation-not-found)
      </td>

      <td style={{ textAlign: "left" }}>
        Org operation not found
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        5C
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        57
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [OOT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#oot---orgs-operation-timeout)
      </td>

      <td style={{ textAlign: "left" }}>
        Orgs operation timeout
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [OP1](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#op1---message-consistency-or-generic-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Generic error
      </td>

      <td style={{ textAlign: "left" }}>
        Both
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        05
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        05
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [OP1](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#op1---message-consistency-or-generic-error)
      </td>

      <td style={{ textAlign: "left" }}>
        Incomplete transaction
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        12
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        30
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [OP1](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#op1---message-consistency-or-generic-error)
      </td>

      <td style={{ textAlign: "left" }}>
        PIN translation failed
      </td>

      <td style={{ textAlign: "left" }}>
        SL
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        05
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [PAE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#pae---unexpected-error-while-fetching-parameters)
      </td>

      <td style={{ textAlign: "left" }}>
        Unexpected error while fetching parameters
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [PAT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#pat---a-timeout-occurred-while-fetching-parameters)
      </td>

      <td style={{ textAlign: "left" }}>
        A timeout occurred while fetching parameters
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        * <br />
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [PCE](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#pce---unexpected-error-in-processing-code-definition)
      </td>

      <td style={{ textAlign: "left" }}>
        Unexpected error in processing code definition
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        02
      </td>

      <td style={{ textAlign: "left" }}>
        N0
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        06
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>

      <td style={{ textAlign: "left" }}>
        96
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [PCT](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#pct---a-timeout-occurred-in-processing-code-definition)
      </td>

      <td style={{ textAlign: "left" }}>
        A timeout occurred in processing code definition
      </td>

      <td style={{ textAlign: "left" }}>
        SF
      </td>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/validation-codes-for-authorization-events.md`: updatedAt 2026-08-06T02:48:36.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/validation-codes-for-authorization-events.md` | body lines 1–3005 | https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events | `dc858d8fce832628…` | 2026-08-06T02:48:36.000Z |

## Related knowledge units

- `KU-ERR-validation-code-definitions` — Validation code definitions
