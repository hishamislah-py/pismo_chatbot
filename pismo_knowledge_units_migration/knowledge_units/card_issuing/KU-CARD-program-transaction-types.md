---
ku_id: KU-CARD-program-transaction-types
title: Program transaction types
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/program-transaction-types.md
  sha256: 22d8603a4a559c84cddff94d223bd7898b3876f02e6ebd1385d1f2a22f56e121
  url: https://developers.pismo.io/pismo-docs/docs/program-transaction-types
  role: primary_guide
  updated_at: '2026-05-08T17:54:05.000Z'
operations:
- createProgramTransactionType
related_kus:
- KU-API-revolving-credit-configurations--program-transaction-types
grouping_rationale: single source page
---

# Program transaction types

**KU ID:** `KU-CARD-program-transaction-types` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/program-transaction-types.md`:

> Use a program transaction type to unite a [program transaction category](https://developers.pismo.io/pismo-docs/docs/program-transaction-categories), a [transaction type](https://developers.pismo.io/pismo-docs/docs/transaction-types), and a program.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/program-transaction-types.md`: Program transaction types

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/program-transaction-types.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/program-transaction-types · updatedAt: 2026-05-08T17:54:05.000Z

<!-- source:begin path=docs/card-issuing/program-transaction-types.md part=0-end -->

# Program transaction types

Use a program transaction type to unite a [program transaction category](https://developers.pismo.io/pismo-docs/docs/program-transaction-categories), a [transaction type](https://developers.pismo.io/pismo-docs/docs/transaction-types), and a program.

Define program transaction types at the program level using the [Create program transaction type](https://developers.pismo.io/pismo-docs/reference/createprogramtransactiontype) endpoint or the Pismo Control Center. For creation through the Control Center, refer to <Anchor label="Create processing codes and transaction types" target="_blank" href="doc:create-processing-codes-and-transaction-types">Create processing codes and transaction types</Anchor>.

Multiple program transaction types can link to the same transaction type. In this way, different programs can use the same transaction type. However, that transaction type links to a different program transaction category for each program (via the program transaction type).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/programs/{programId}/program-transaction-types` | `createProgramTransactionType` | Create program transaction type | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-transaction-types |

### Operation essentials

- **`POST /v1/programs/{programId}/program-transaction-types`** (`createProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EX0001`, `EX0002`; events none listed.

## Lifecycle status

- `docs/card-issuing/program-transaction-types.md`: updatedAt 2026-05-08T17:54:05.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/program-transaction-types.md` | whole document | https://developers.pismo.io/pismo-docs/docs/program-transaction-types | `22d8603a4a559c84…` | 2026-05-08T17:54:05.000Z |

## Related knowledge units

- `KU-API-revolving-credit-configurations--program-transaction-types` — API reference: Revolving credit - Configurations — Program transaction types
