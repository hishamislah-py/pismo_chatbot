---
ku_id: KU-CC-embossing-in-control-center
title: Embossing
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/embossing-in-control-center.md
  sha256: 9e21248b7af89f7d43ee6ba66941cc1da363c9c50938316633e8fb42a99e45e9
  url: https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center
  role: primary_guide
  updated_at: '2026-08-03T14:30:32.000Z'
operations: []
related_kus:
- KU-CARD-physical-card-embossing
grouping_rationale: single source page
---

# Embossing

**KU ID:** `KU-CC-embossing-in-control-center` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/embossing-in-control-center.md`:

> Use Control Center to manage embossing configurations, such as the embossing schedule and the programs associated with specific configurations. Embossing is the process of adding raised or recessed details—like names, card numbers, and expiration dates—to a card for personalization and branding. It enhances both the card’s functionality and visual appeal. For more information, refer to [Physical card embossing](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/embossing-in-control-center.md`: Embossing; Create an embossing configuration; Edit an existing embossing configuration; Change the embossing schedule; Associate  a program with an embossing configuration; From programs; From embossing; Remove a program from an embossing configuration; From programs; From embossing; Define an alias

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/embossing-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center · updatedAt: 2026-08-03T14:30:32.000Z

<!-- source:begin path=docs/control-center/embossing-in-control-center.md part=0-end -->

# Embossing 

Use Control Center to manage embossing configurations, such as the embossing schedule and the programs associated with specific configurations. Embossing is the process of adding raised or recessed details—like names, card numbers, and expiration dates—to a card for personalization and branding. It enhances both the card’s functionality and visual appeal. For more information, refer to [Physical card embossing](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing).

# Create an embossing configuration

You must work with your Pismo representative to create a new embossing configuration.

1. From the main menu, select **Configurations** > **Embossing**.
2. Use the links in the notification to first download a configuration spreadsheet and then open a Service Desk request. Your Pismo representative will help you complete the configuration spreadsheet and create your new configuration.

<Image align="center" alt="Links to download the configuration spreadsheet and open a Service Desk request" border={true} src="https://files.readme.io/4563a80bda86e817cc93eb5de1f6caee50d6ea38cca69709403ba368851b01f0-Screenshot_2025-08-15_at_9.49.59_AM.png" className="border" />

# Edit an existing embossing configuration

For existing embossing configurations, you can change these settings in Control Center.

| Setting             | How you can use it                                                    | For more help                                                                                                                                                                                                                                                                       |
| :------------------ | :-------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Embossing schedule  | Specify the days and times embossing jobs run                         | [Change the embossing schedule](https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center-beta#change-the-embossing-schedule)                                                                                                                                                                                 |
| Associated programs | Assign specific embossing configurations to your programs             | [Associate a program with an embossing configuration](https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center#associate-a-program-with-an-embossing-configuration) and [Remove a program from an embossing configuration](https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center#remove-a-program-from-an-embossing-configuration) |
| Alias               | Specify an alternate name for a program to make it easier to identify | [Define an alias](https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center#define-an-alias)                                                                                                                                                                                                                  |

To change any other setting, you must work with your Pismo representative. In Control Center, use the links in the notification to first download a configuration spreadsheet and then open a Service Desk request. Your Pismo representative will help you complete the configuration spreadsheet and update your existing configuration.

<Image align="center" alt="Links to download the configuration spreadsheet for existing configurationsand open a Service Desk request" src="https://files.readme.io/3be0a5a8a7537d8e8e1eba68f31dec26fa5a66c1e6506e1f34d69dfdf583d9d2-Screenshot_2025-08-15_at_10.11.40_AM.png" />

## Change the embossing schedule

To change the embossing schedule, do the following:

1. From the main menu, select **Configurations** > **Embossing**.
2. On the **Embossing** screen, select the embossing configuration.
3. On the **Embossing details** screen, select **Edit**.
4. Change the required details in the embossing wizard and select **Update schedule**.

## Associate  a program with an embossing configuration

There are two ways to associate a program with an embossing configuration.

### From programs

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Programs** screen, select the program.
3. On the **Program information** screen, select the **Embossing** tab.
4. Select **Add embossing**.
5. Enter the required details in the embossing wizard and select **Add configuration**.

### From embossing

1. From the main menu, select **Configurations** > **Embossing**.
2. On the **Embossing** screen, select the embossing configuration.
3. On the **Embossing details** screen, select **Add programs**.
4. Enter the required details in the programs wizard and select **Add programs**.

## Remove a program from an embossing configuration

There are two ways to remove a program from an embossing configuration.

### From programs

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Programs** screen, select the program.
3. On the **Program information** screen, select the **Embossing** tab.
4. Select **Remove this embossing configuration from the program** and then confirm.

### From embossing

1. From the main menu, select **Configurations** > **Embossing**.
2. On the **Embossing** screen, select the embossing configuration.
3. On the **Embossing details** screen, select the trash icon next to the program and then confirm.

## Define an alias

To specify an alternate name for a program to make it easier to identify, you can define an alias.

1. From the main menu, select **Configurations** > **Embossing**.
2. On the **Embossing** screen, select the embossing configuration.
3. On the **Embossing details** screen, select **Edit**.
4. Enter an alias name and select **Save**.
<!-- source:end -->

## Lifecycle status

- `docs/control-center/embossing-in-control-center.md`: updatedAt 2026-08-03T14:30:32.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/embossing-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center | `9e21248b7af89f7d…` | 2026-08-03T14:30:32.000Z |

## Related knowledge units

- `KU-CARD-physical-card-embossing` — Physical card embossing
