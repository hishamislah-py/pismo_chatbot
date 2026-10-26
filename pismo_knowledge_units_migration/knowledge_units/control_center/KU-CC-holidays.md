---
ku_id: KU-CC-holidays
title: Holidays
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/holidays.md
  sha256: 742059bda59cd98850d0bd79511e2bfa092974c97d55602374b3b2f3f32e2ba7
  url: https://developers.pismo.io/pismo-docs/docs/holidays
  role: primary_guide
  updated_at: '2026-08-31T17:22:44.000Z'
operations: []
related_kus:
- KU-CORE-platform-setup-holidays
grouping_rationale: single source page
---

# Holidays

**KU ID:** `KU-CC-holidays` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/holidays.md`:

> Use holiday calendars to define working days and holidays for your organization on the Pismo platform. By default, the Pismo platform processes transactions every day, but you might need to restrict transactions on certain days, such as holidays, weekends, or other non-working days.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/holidays.md`: Holidays; View holiday calendars; Calendar tab; Hierarchy tab; Create and manage holiday calendars; Create a calendar; Edit a calendar; Export a calendar; Delete a calendar; Add, edit, and delete holidays

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/holidays.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/holidays · updatedAt: 2026-08-31T17:22:44.000Z

<!-- source:begin path=docs/control-center/holidays.md part=0-end -->

# Holidays

Use holiday calendars to define working days and holidays for your organization on the Pismo platform. By default, the Pismo platform processes transactions every day, but you might need to restrict transactions on certain days, such as holidays, weekends, or other non-working days.

For more in-depth information, refer to the  [Platform setup - Holidays and administrative divisions](https://developers.pismo.io/pismo-docs/docs/platform-setup-holidays) guide.

From Control Center, you can do the following:

* [View holiday calendars](https://developers.pismo.io/pismo-docs/docs/holidays#view-holiday-calendars)
* [Create and manage holiday calendars](https://developers.pismo.io/pismo-docs/docs/holidays#create-and-manage-holiday-calendars)
* [Add, edit, and delete holidays](https://developers.pismo.io/pismo-docs/docs/holidays#add-edit-and-delete-holidays)

# View holiday calendars

To view holiday calendars:

1. From the main menu, select  **Configurations** > **Holidays**.\
   A list of holiday calendars is displayed. You can search for a specific calendar by name or tag. Tags group calendars to make them easier to find, such as all calendars for a specific city.

2. Select a calendar to open its details. The **Calendar details** screen is displayed.

<Image align="center" alt="Holiday calendar in Control Center calendar tab" border={true} width="200% " src="https://files.readme.io/2d99cc6a42d25e6a0dc998de3e72d7167aad7d7059aff1f5c9ee1430a8028c57-Holiday_calendar_-_Calendar_tab.png" className="border" />

The following sections describe what you can do on this screen.

## Calendar tab

On the **Calendar tab**, you can do the following:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Item
      </th>

      <th>
        Description
      </th>

      <th>
        For more information
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1—Calendar and Hierarchy tabs
      </td>

      <td>
        Switch between an overview of the holiday calendar and details about the hierarchy.
      </td>

      <td>
        [Hierarchy tab](https://developers.pismo.io/pismo-docs/docs/holidays#hierarchy-tab)
      </td>
    </tr>

    <tr>
      <td>
        2–Edit icon
      </td>

      <td>
        Wherever this icon appears, you can make changes.
      </td>

      <td>
        [Edit a calendar](https://developers.pismo.io/pismo-docs/docs/holidays#edit-a-calendar)\
        [Add, edit, and delete holidays](https://developers.pismo.io/pismo-docs/docs/holidays#add-edit-and-delete-holidays)
      </td>
    </tr>

    <tr>
      <td>
        3–See full hierarchy link
      </td>

      <td>
        View the complete calendar hierarchy screen
      </td>

      <td>
        [Hierarchy tab](https://developers.pismo.io/pismo-docs/docs/holidays#hierarchy-tab)
      </td>
    </tr>

    <tr>
      <td>
        4–Show parents slider
      </td>

      <td>
        Expand the list of holidays to show parent holidays
      </td>

      <td />
    </tr>

    <tr>
      <td>
        5–Date range
      </td>

      <td>
        Show holidays in a specific date range. To show all holidays, leave the dates blank
      </td>

      <td />
    </tr>

    <tr>
      <td>
        6–Add holiday button
      </td>

      <td>
        Add a holiday
      </td>

      <td>
        [Add, edit, and delete holidays](https://developers.pismo.io/pismo-docs/docs/holidays#add-edit-and-delete-holidays)
      </td>
    </tr>

    <tr>
      <td>
        7–Delete holiday icon
      </td>

      <td>
        Delete a holiday
      </td>

      <td>
        [Add, edit, and delete holidays](https://developers.pismo.io/pismo-docs/docs/holidays#add-edit-and-delete-holidays)
      </td>
    </tr>

    <tr>
      <td>
        8-Delete calendar button
      </td>

      <td>
        Delete a calendar
      </td>

      <td>
        [Delete a calendar](https://developers.pismo.io/pismo-docs/docs/holidays#delete-a-calendar)
      </td>
    </tr>

    <tr>
      <td>
        9—Working days
      </td>

      <td>
        Select the days of the week when transactions are allowed
      </td>

      <td />
    </tr>
  </tbody>
</Table>

## Hierarchy tab

On the **Hierarchy** tab, you can view the hierarchy associated with a holiday calendar. A **hierarchy** organizes divisions—regional, organizational, and so on—into parent-child relationships. This structure allows child divisions to inherit settings from parent divisions.

In this example, Rome inherits all holidays assigned to the Lazio region, and Lazio inherits all holidays assigned to Italy. Rome can also have its own holidays specific to the city.

To view and edit an associated calendar, select **View details**.

<Image align="center" alt="Hierarchy tab on the Calendar details screen" border={true} src="https://files.readme.io/51d45ca6246017bf954c0c5d3136b0346c4df2e22ec26088f2e9d149d939a6eb-Screenshot_2026-08-07_at_4.43.41_PM.png" className="border" />

# Create and manage holiday calendars

You can create a new holiday calendar or import one that was previously exported from another organization or environment. For example, when promoting a configuration from sandbox to production, export the holiday calendar from the sandbox environment and import it into the production environment.

The following sections explain how to create, edit, export, and delete holiday calendars.

## Create a calendar

To create a new calendar or import an existing one.

1. From the main menu, select  **Configurations** > **Holidays**.\
   The **Holidays** screen is displayed.

<Image align="center" alt="Create calendar button and export-import menu items" border={true} src="https://files.readme.io/2cecd8e58bb602d015b2097325cfdcae0622c5e64aef13d52c97b26c1c324f2b-Screenshot_2026-08-07_at_12.21.07_PM.png" className="border" />

2. On the **Holidays** screen:

* **Create a new calendar**—Select **Create calendar** and complete the wizard.
* **Import an existing calendar**—From the actions menu, select **Import** and upload a holiday calendar as a JSON file. You'll get a notification once the calendar is ready, which can take up to four hours.

## Edit a calendar

Wherever the edit icon (pencil) appears, you can make changes, including:

* **Calendar name**—Enter a new name
* **Tag**—Select an existing tag or enter a new one. Tags groups calendars to make them easier to find.
* **External ID**—Enter an External ID, which is an identifier used to reference a resource in a system external to Pismo. It can be up to 36 characters.
* **Working days**—Change working days, which are the days when transactions are allowed.
* **Next parent level**—Select a new parent for this calendar in the hierarchy. For more information, refer to [Hierarchy tab](https://developers.pismo.io/pismo-docs/docs/holidays#hierarchy-tab).

## Export a calendar

You can export calendars and import them in another organization or environment, removing the need to manually recreate them.

To export a calendar, from the actions menu, select **Export**. When the export is complete, you receive a notification like the one shown here. The export file is available for download for seven days. After it expires, you'll need to export the calendar again.

<Image align="center" alt="Notification that the calendar is ready to download" border={true} src="https://files.readme.io/b72fd069d7ef8808de40467147613e72e46568a2fbf9fa5c714a2e525b4656fe-Download.png" className="border" />

## Delete a calendar

To delete a calendar:

1. From the main menu, select  **Configurations** > **Holidays**.
2. Select **Delete calendar**. If the button is grayed out, you can't delete the calendar because it still contains holidays or has linked parent or child calendars. Remove the holidays and unlink any related calendars, then try again.

# Add, edit, and delete holidays

On the **Calendar details** screen, you can add holidays, edit their names, and delete them.

* **Add a holiday**—Select **Add holidays** and complete the wizard.
* **Edit a holiday's name**—Select the edit icon (pencil) on the holiday you want to edit.
* **Delete a holiday**—Select the delete icon (trash can) on the holiday you want to delete. If the icon is grayed out, you can't delete the holiday because it's either today or in the past. You can only delete future holidays.

<br />

<br />

<br />
<!-- source:end -->

## Lifecycle status

- `docs/control-center/holidays.md`: updatedAt 2026-08-31T17:22:44.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/holidays.md` | whole document | https://developers.pismo.io/pismo-docs/docs/holidays | `742059bda59cd988…` | 2026-08-31T17:22:44.000Z |

## Related knowledge units

- `KU-CORE-platform-setup-holidays` — Platform setup - Holidays and administrative divisions
