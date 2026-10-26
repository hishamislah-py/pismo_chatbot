---
ku_id: KU-CC-copy-configurations
title: Copy configurations
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/copy-configurations.md
  sha256: 1a93865bea2214d31670e9075b0d09f66708fc8cdd0269410f49a6a188bf3f4d
  url: https://developers.pismo.io/pismo-docs/docs/copy-configurations
  role: primary_guide
  updated_at: '2026-08-07T11:15:29.000Z'
operations: []
related_kus:
- KU-CC-holidays
grouping_rationale: single source page
---

# Copy configurations

**KU ID:** `KU-CC-copy-configurations` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/copy-configurations.md`:

> View and manage your copied Control Center feature configurations. With the copy configurations feature, you can:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/copy-configurations.md`: Copy configurations; View copied configurations; Import details screen; Understanding existing and new records; Export details screen; Download a configuration; Import a configuration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/copy-configurations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/copy-configurations · updatedAt: 2026-08-07T11:15:29.000Z

<!-- source:begin path=docs/control-center/copy-configurations.md part=0-end -->

# Copy configurations

View and manage your copied Control Center feature configurations. With the copy configurations feature, you can:

* Reuse existing configurations across Control Center environments, removing the need to recreate them manually
* Monitor the progress and outcome of your imports and exports
* View the history of imported and exported configurations across your organization
* Troubleshoot failed imports and exports through dedicated details screens

<Accordion title="Copy configurations supports the following features:">
  <ul>
    <li><a href="https://developers.pismo.io/pismo-docs/docs/holidays">Holidays</a></li>
  </ul>
</Accordion>

From Control Center, you can do the following:

* [View copied configurations](#view-copied-configurations)
* [Download a configuration](#download-a-configuration)
* [Import a configuration](#import-a-configuration)

# View copied configurations

To view the list of copied configurations and explore an entry in more detail, do the following:

1. From the main menu, select **Configurations** > **Copy configurations**.
2. On the **Copy configurations** screen, select an entry. Use the filter options to refine the list.

<Image align="center" alt="Screenshot showing the Copy configurations screen" border={true} src="https://files.readme.io/31a60afe58f0286a4ca5b388af75e8143afac1b217ab226487a24ac5cebb4aa8-copy-configurations.png" className="border" />

The **Copy configurations** screen displays the list of copied configurations for the Control Center environment. Each entry represents a configuration imported to or exported from the environment.

Successfully exported configurations include a download icon, which you can select to download a JSON file of the configuration. For more information, refer to [Download a configuration](#download-a-configuration).

> 📘 Exporting a configuration
>
> You cannot export a configuration from the **Copy configurations** screen. To export a configuration, you must go to the specific feature menu.

A configuration can have one of the following statuses:

* **Processing**—The file import or export is in progress.
* **Done**—The file import or export completed successfully.
* **Failed**—The file import or export failed.
* **Expired** (export only)—The download link for the exported file expired. For more information, refer to [Download a configuration](#download-a-configuration).

The following sections describe the **Import details** and **Export details** screens in more detail.

## Import details screen

The **Import details** screen displays information about the import. You can view the import progress of individual configuration components and review the number of existing and new records for each component.

<Image align="center" alt="Screenshot showing the Import details screen" border={true} src="https://files.readme.io/5884777a7c6249f8a3617da0d2aef16931419a92941520ca816086778d9db1f4-import-details-screen.png" className="border" />

The **Steps** section divides the import into individual configuration components, giving you a detailed breakdown of each stage of the import process.

All components must import successfully for the overall import to succeed. If even a single component fails, Control Center stops the entire import process. In the event of a failed import, you can review the outcome of individual steps to identify the affected component and troubleshoot the issue.

For more information about the **Steps** section, refer to the following table.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **COMPONENTS**
      </td>

      <td>
        A grouping of related configuration data
      </td>
    </tr>

    <tr>
      <td>
        **RECORDS**
      </td>

      <td>
        The number of data elements contained in the component
      </td>
    </tr>

    <tr>
      <td>
        **EXISTING**
      </td>

      <td>
        The number of records that already exist in the target environment. This data is not imported.
      </td>
    </tr>

    <tr>
      <td>
        **NEW**
      </td>

      <td>
        The number of records that do not exist in the target environment. This data is imported as part of the configuration.
      </td>
    </tr>

    <tr>
      <td>
        **STATUS**
      </td>

      <td>
        The import status of the component

        * **Processing**—The component import is in progress.
        * **Done**—The component import completed successfully.
        * **Failed**—The component import failed.
      </td>
    </tr>
  </tbody>
</Table>

### Understanding existing and new records

The **EXISTING** and **NEW** columns help you understand how the imported configuration relates to the data already present in the target environment.

For example, if a holiday configuration contains records for Christmas Day and New Year's Day, but the target environment already includes the Christmas Day record:

* **EXISTING** displays **1**
* **NEW** displays **1**

During the import, only the New Year's Day record is imported.

## Export details screen

The **Export details** screen displays information about the export. You can view the export progress of individual configuration components and [download](#download-a-configuration) completed exports.

<Image align="center" alt="Screenshot showing the export details screen" border={true} src="https://files.readme.io/24e4a5b01da2c5bfd1b26be13ade867f4f42bfc3e1e8d73dd644b5f46c080d9e-export-details-screen.png" className="border" />

The **Steps** section divides the export into individual configuration components, giving you a detailed breakdown of each stage of the export process.

All components must export successfully for the overall export to succeed. If even a single component fails, Control Center stops the entire export process. In the event of a failed export, you can review the outcome of individual steps to identify the affected component and troubleshoot the issue.

For more information about the **Steps** section, refer to the following table.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **COMPONENTS**
      </td>

      <td>
        A grouping of related configuration data
      </td>
    </tr>

    <tr>
      <td>
        **RECORDS**
      </td>

      <td>
        The number of data elements contained in the component
      </td>
    </tr>

    <tr>
      <td>
        **STATUS**
      </td>

      <td>
        The export status of the component

        * **Processing**—The component export is in progress.
        * **Done**—The component export completed successfully.
        * **Failed**—The component export failed.
      </td>
    </tr>
  </tbody>
</Table>

# Download a configuration

Download a JSON file of your exported configuration to save it for offline storage and future use.

Before downloading a configuration, note the following:

* The option to download is available only when the configuration export status is **Done**.
* You have 7 days to download the file. After that, you'll need to export the configuration again.

To download an exported configuration, on the **Copy configurations** screen, select the download icon for the configuration you want to download. You can also download the configuration from the **Export details** screen.

# Import a configuration

Import a previously exported configuration to reuse it across your Control Center environments. Import a configuration to:

* Promote a sandbox configuration to a live production environment
* Maintain consistency across selected environments
* Restore an earlier version of a configuration

> 🚧  Editing configuration files outside of Control Center
>
> Do not edit configuration files outside of Control Center.
>
> Control Center validates the structure and integrity of configuration files during the import process. If you try to import an altered file, the import fails.

To import a configuration, from the **Copy configurations** screen, select **Import** and upload your configuration file. Imported configurations are automatically added to their respective feature menu. For example, if you import a holiday configuration, it's added as an entry to the [Holidays](https://developers.pismo.io/pismo-docs/docs/holidays) configuration menu.

<br />
<!-- source:end -->

## Lifecycle status

- `docs/control-center/copy-configurations.md`: updatedAt 2026-08-07T11:15:29.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/copy-configurations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/copy-configurations | `1a93865bea2214d3…` | 2026-08-07T11:15:29.000Z |

## Related knowledge units

- `KU-CC-holidays` — Holidays
