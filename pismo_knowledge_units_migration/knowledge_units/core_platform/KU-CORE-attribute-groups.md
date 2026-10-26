---
ku_id: KU-CORE-attribute-groups
title: Attribute groups
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/attribute-groups.md
  sha256: ef7edd2f94359e97099abb091e742341753b3407cf8a678a09a66c5dac520b2d
  url: https://developers.pismo.io/pismo-docs/docs/attribute-groups
  role: primary_guide
  updated_at: '2026-09-29T22:55:38.000Z'
operations:
- get-v1-attribute-groups
- get-v1-attribute-groups-groupId
- post-v1-accounts-flex-controls
- post-v1-attribute-group-flex-controls
- post-v1-customers-flex-controls
- update-v1-attribute-groups
related_kus:
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-flex-controls--attribute-groups
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-CC-flex-controls
- KU-CORE-flex-controls
- KU-EVT-catalogue-audit
grouping_rationale: single source page
---

# Attribute groups

**KU ID:** `KU-CORE-attribute-groups` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/attribute-groups.md`:

> Flexible transaction controls support attribute groups, which allow you to define sets of values, such as merchant IDs or Merchant Category Codes (MCCs), that can be shared across multiple controls within the same organization. This feature simplifies control configuration and significantly improves maintainability.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/attribute-groups.md`: Attribute groups; Create attribute group; Reference attribute group in flex controls; Manage attribute groups; Authorization workflow integration; Best practices; Related topics

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/attribute-groups.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/attribute-groups · updatedAt: 2026-09-29T22:55:38.000Z

<!-- source:begin path=docs/core-platform/attribute-groups.md part=0-end -->

# Attribute groups

Flexible transaction controls support attribute groups, which allow you to define sets of values, such as merchant IDs or Merchant Category Codes (MCCs), that can be shared across multiple controls within the same organization. This feature simplifies control configuration and significantly improves maintainability.

You create attribute groups at the organization level and can share them across all entities within the same organization (programs, accounts, customers, and cards). This centralized approach promotes consistency, simplifies control management across different scopes, and ensures that the control logic dynamically evaluates the group values during the authorization workflow. When you update an attribute group, the platform automatically reflects this change across all flex controls that reference it, enabling efficient bulk updates.

To enable this functionality, you must first [create an attribute group](https://developers.pismo.io/pismo-docs/reference/post-v1-attribute-group-flex-controls) and then reference it in flex controls using the new operators: `in_group` and `not_in_group`. These operators allow the control to evaluate whether a transaction attribute matches any value within the defined group.

During the authorization workflow, the flex controls engine evaluates incoming payload attributes against the values defined in the referenced group. If a match is found, the condition is satisfied. If no match is found, the condition fails.

# Create attribute group

To create an attribute group, use the [Create attribute group](https://developers.pismo.io/pismo-docs/reference/post-v1-attribute-group-flex-controls) endpoint.

<Callout icon="📘" theme="info">
  Currently, there is no user interface, such as Control Center, to manage attribute groups within flex controls. All operations must be performed via the API.
</Callout>

Each attribute group must include the following.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `id`
      </td>

      <td>
        Attribute group ID, unique within the organization (maximum 36 characters).
      </td>
    </tr>

    <tr>
      <td>
        `description`
      </td>

      <td>
        A short description of the attribute group (maximum 50 characters).
      </td>
    </tr>

    <tr>
      <td>
        `type`
      </td>

      <td>
        Must correspond to an existing attribute supported by flex controls. At this time, `merchant_id`  and `merchant_category_code` are supported.
      </td>
    </tr>

    <tr>
      <td>
        `values`
      </td>

      <td>
        An array of unique values representing the grouped items.

        * Each value must be unique within the array
        * Maximum of 20,000 items
        * Each item must not exceed 15 characters
      </td>
    </tr>
  </tbody>
</Table>

This structure allows the group to be referenced across multiple flex controls within the same organization.

The following example request payload of the [Create attribute group](https://developers.pismo.io/pismo-docs/reference/post-v1-attribute-group-flex-controls) endpoint defines the attribute group of non-trusted merchants.

```json
{  
    "id": "non-trusted-merchants",  
    "description": "High-risk merchant IDs",  
    "type": "merchant_id",  
    "values": [  
        "0001",  
        "0010",  
        "0002"  
    ]  
}
```

# Reference attribute group in flex controls

Once you create an attribute group, you reference it in flex controls in the `conditions` configuration in the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) or [Create customer flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls) endpoint.

* In the `operator` field, use the operators `in_group` or `not_in_group`.
* In the `value` field, include the attribute group ID.

The following example request payload of the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) or [Create customer flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls)  endpoint uses the previously defined attribute group of non-trusted merchants to restrict operations with those merchants.

```json
{  
    "name": "non_trusted_merchant_restriction",  
    "type": "restriction",  
    "deny_code": "merchant_not_allowed",  
    "conditions": [  
       {  
         "attribute": "merchant_id",  
         "operator": "in_group",  
         "value": "non-trusted-merchants"  
    }  
  ]  
}
```

For more details on how to create flex controls at different levels, refer to the following documentation:

* [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls)
* [Flex controls in Control Center](https://developers.pismo.io/pismo-docs/docs/cc-flex-controls)

# Manage attribute groups

To update the `values` field in an attribute group, use the [Update attribute group](https://developers.pismo.io/pismo-docs/reference/update-v1-attribute-groups) endpoint.

To return all details of the attribute group specified by its ID, use the [Get attribute group](https://developers.pismo.io/pismo-docs/reference/get-v1-attribute-groups-groupid) endpoint.

To list all available attribute groups, use the [List attribute group](https://developers.pismo.io/pismo-docs/reference/get-v1-attribute-groups) endpoint. You can optionally provide the `limit` query parameter to specify the maximum number of groups to return per page.

# Authorization workflow integration

During the authorization process, the platform evaluates the payload against the configured flex controls. When a condition references a group, the platform performs the following steps:

* Identifies the relevant attribute in the incoming payload (for example, `merchant_id`)
* Checks whether the attribute value exists within the referenced group
* Applies the control logic based on the result of this evaluation

This mechanism ensures that group-based conditions are evaluated dynamically and consistently during real-time authorizations, allowing for flexible and centralized control logic.

# Best practices

* Use clear, descriptive IDs for groups (for example, `trusted_merchants`, `high_risk_mccs`).
* Validate the attribute group's existence before referencing it in flex controls.
* Test the attribute group behavior in the sandbox environment before configuring it in production.
* Keep group values updated to reflect business logic changes.

## Related topics

[Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls)

[Simulate flex control creation](https://developers.pismo.io/pismo-docs/docs/simulate-flex-control-creation)

[Flex controls use cases](https://developers.pismo.io/pismo-docs/docs/flex-controls-use-cases)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/attribute-groups` | `post-v1-attribute-group-flex-controls` | Create attribute group | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |
| `POST /v1/accounts/{accountId}/flex-controls` | `post-v1-accounts-flex-controls` | Create account flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/customers/{customerId}/flex-controls` | `post-v1-customers-flex-controls` | Create customer flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01 |
| `PATCH /v1/attribute-groups/{groupId}` | `update-v1-attribute-groups` | Update attribute group | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |
| `GET /v1/attribute-groups/{groupId}` | `get-v1-attribute-groups-groupId` | Get attribute group | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |
| `GET /v1/attribute-groups` | `get-v1-attribute-groups` | List attribute groups | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |

### Operation essentials

- **`POST /v1/attribute-groups`** (`post-v1-attribute-group-flex-controls`): security `BearerAuth`; required parameters none declared; required body fields `id`, `description`, `type`, `values`; response statuses 201, 400, 409, 500; error codes in examples `ERUL0707`, `RULVAL0400`, `ERUL0001`, `RULREP0500`; events none listed.
- **`POST /v1/accounts/{accountId}/flex-controls`** (`post-v1-accounts-flex-controls`): security `BearerAuth`; required parameters `accountId` (path); required body fields `type`, `name`, `deny_code`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL0701`, `RULVAL0400`, `ERUL0702`, `ERUL0703`, `ERUL0704`, `ERUL0706`, `ERUL0004`, `ERUL0002`, `RULVAL0403`, `WRUL0707`, `RULVAL0409`, `ERUL0001`, `RULREP0500`; events `audit-account-spending-limit-created-1`.
- **`POST /v1/customers/{customerId}/flex-controls`** (`post-v1-customers-flex-controls`): security `BearerAuth`; required parameters `customerId` (path); required body fields `type`, `name`, `account_id`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL1101`, `RULVAL0400`, `ERUL1102`, `ERUL1106`, `ERUL0002`, `RULVAL0403`, `WRUL1207`, `RULVAL0409`, `ERUL0005`, `RULREP0500`, `ERUL1105`; events `audit-customer-spending-limit-created-1`.
- **`PATCH /v1/attribute-groups/{groupId}`** (`update-v1-attribute-groups`): security `BearerAuth`; required parameters `groupId` (path); required body fields `values`; response statuses 204, 400, 404; error codes in examples `ERUL0806`, `RULVAL0400`, `ERUL0805`, `RULVAL0400`; events none listed.
- **`GET /v1/attribute-groups/{groupId}`** (`get-v1-attribute-groups-groupId`): security `BearerAuth`; required parameters `groupId` (path); required body fields none declared; response statuses 200, 404; error codes in examples `ERUL0805`, `RULVAL0400`; events none listed.
- **`GET /v1/attribute-groups`** (`get-v1-attribute-groups`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200; error codes in examples none; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-accounts-flex-controls` | `audit-account-spending-limit-created-1` |
| `post-v1-customers-flex-controls` | `audit-customer-spending-limit-created-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/attribute-groups.md`: updatedAt 2026-09-29T22:55:38.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/attribute-groups.md` | whole document | https://developers.pismo.io/pismo-docs/docs/attribute-groups | `ef7edd2f94359e97…` | 2026-09-29T22:55:38.000Z |

## Related knowledge units

- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-flex-controls--attribute-groups` — API reference: Core platform - Flex controls — Attribute groups
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-CC-flex-controls` — Control Center flex controls, with a Pix example
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-EVT-catalogue-audit` — Event catalogue: audit
