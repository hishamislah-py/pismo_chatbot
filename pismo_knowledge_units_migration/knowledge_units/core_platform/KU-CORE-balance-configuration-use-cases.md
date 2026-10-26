---
ku_id: KU-CORE-balance-configuration-use-cases
title: Balance configuration use cases
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/balance-configuration-use-cases.md
  sha256: c65147305d770c58a98df694f8975b5fdf86462030622eedcf4d429538fba67e
  url: https://developers.pismo.io/pismo-docs/docs/balance-configuration-use-cases
  role: primary_guide
  updated_at: '2026-03-18T15:14:37.000Z'
operations: []
related_kus:
- KU-CC-balance-configurations
- KU-CORE-balance-configurations
grouping_rationale: single source page
---

# Balance configuration use cases

**KU ID:** `KU-CORE-balance-configuration-use-cases` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/balance-configuration-use-cases.md`:

> Banking account cash-out is the default configuration for handling cash-out from the main available balance. You can apply it at the organization, program, or account level for all cash-out authorizations.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/balance-configuration-use-cases.md`: Balance configuration use cases; Configure banking account cash-out limit; Configure credit card purchase limits; Configure credit card withdrawal limit; Adjust available credit limit based on transaction spending; Configure installment purchase using installment limit; Manage credit limits based on number of installments; Related topics

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/balance-configuration-use-cases.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/balance-configuration-use-cases · updatedAt: 2026-03-18T15:14:37.000Z

<!-- source:begin path=docs/core-platform/balance-configuration-use-cases.md part=0-end -->

# Balance configuration use cases

# Configure banking account cash-out limit

Banking account cash-out is the default configuration for handling cash-out from the main available balance. You can apply it at the organization, program, or account level for all cash-out authorizations.

The following payload is a sample of a banking account cash-out operation limit configuration.

* The `tenant` in the `level` field indicates that the configuration applies at the organization level. Note that if any program or account within the organization has a configuration defined at the program or account level, the platform skips this organization-level configuration.
* The `filters` object indicates that the configuration applies to withdrawals with the processing code of `01`.
* The `scenarios` object lists one default `condition` and defines the following in the `result` object:
  * The value in the `impact` field indicates that the platform debits the `AvailableCreditLimit` during the cash-out operation.
  * The value in the `consider` field indicates that the platform uses the `AvailableCreditLimit` to validate whether the account has sufficient funds.
  * The value in the `amount` field indicates that the platform uses the `contract_amount` (final amount that includes any interest and fees) to debit the account limit.

```json
{
    "level": "tenant",
    "configs": [
        {
            "filters": {
                "processing_codes": [
                    "01"
                ]
            },
            "scenarios": [
                {
                    "condition": {
                    	"order": 1,
                        "type": "default"
                    },
                    "result": {
                        "impact": [
                            "AvailableCreditLimit"
                        ],
                        "consider": [
                            "AvailableCreditLimit"
                        ],
                        "amount": "contract_amount"
                    }
                }
            ]
        }
    ]
}
```

In this use case, if there is a cash-out of $30 that has a processing code of 01 on an account in the organization, the account has its available credit limit (`AvailableCreditLimit`) debited by $30. If `AvailableCreditLimit` was $1000, it would be $970 after this cash-out operation.

# Configure credit card purchase limits

You can create configurations for credit card purchases at the organization, program, or account level. The following payload  is a sample of a credit card purchase limit configuration.

* The values in the `level` and `program_id` field define the program for this configuration.
* The `filters` object indicates that the configuration applies to credit card purchases with the processing code of `00`.
* The value in the `impact` field indicates that the platform debits the `AvailableCreditLimit` during the credit card purchase.
* The values in the `consider` field indicate that the platform adds the limits of `AvailableCreditLimit` and `OverLimit` to check if the account has sufficient funds.
* The  value in the `reset_limit` field indicates that the account limit is reset when the customer pays their bill.

```json
{
    "level": "program",
    "program_id": 1234567,
    "configs": [
        {
            "filters": {
                "processing_codes": [
                    "00"
                ]
            },
            "scenarios": [
                {
                    "condition": {
                    	"order": 1,
                        "type": "default"
                    },
                    "result": {
                        "impact": [
                            "AvailableCreditLimit"
                        ],
                        "consider": [
                            "AvailableCreditLimit",
                            "OverLimit"
                        ],
                        "amount": "contract_amount",
                        "reset_limit": "payment"
                    }
                }
            ]
        }
    ]
}
```

In this use case, if there is a transaction for $30 that has a processing code of `00`, the account that belongs to the  `1234567` program has its available credit limit (`AvailableCreditLimit`) debited $30. If `AvailableCreditLimit` was $1000, it would be $970 after this transaction.

# Configure credit card withdrawal limit

The Pismo platform supports withdrawals using a credit card. You can configure a withdrawal limit and an available credit limit. The platform first impacts the withdrawal limit and then the available credit limit. You can apply credit card withdrawal limits at the organization, program, or account level.

The following payload is a sample of a credit card withdrawal limit configuration.

* The values in the `level` and `account_id` field define the account for this configuration.
* The `filters` object indicates that the configuration applies to credit card withdrawals with the processing code of `01`.
* The values in the `impact` field indicate that the platform makes the withdrawal from the `AvailableWithdrawalCredit` and `AvailableCreditLimit`.
* The `AvailableWithdrawalCredit` and `AvailableCreditLimit` values in the `consider` field indicate that the platform separately evaluates both of these limits to validate whether the account has sufficient funds to perform the withdrawal. Also, the `Overlimit` in the `consider` field indicates that if the account has an overlimit set, the platform includes it in the calculation by adding it to the `AvailableCreditLimit`.
* The  value in the `reset_limit` field indicates that both available limits are reset when the customer pays their bill.

```json
{
    "level": "account",
    "account_id": 987654,
    "configs": [
        {
            "filters": {
                "processing_codes": [
                    "01"
                ]
            },
            "scenarios": [
                {
                    "condition": {
                        "order": 1,
                        "type": "default"
                    },
                    "result": {
                        "impact": [
                            "AvailableCreditLimit",
                            "AvailableWithdrawalCredit"
                        ],
                        "consider": [
                            "AvailableCreditLimit",
                            "AvailableWithdrawalCredit",
				                    "OverLimit"
                        ],
                        "amount": "contract_amount",
                        "reset_limit": "payment"
                    }
                }
            ]
        }
    ]
}

```

In this use case, if there is a $100 credit card withdrawal that has a processing code of `01`, the `987654` account has its available credit limit (`AvailableCreditLimit`) and available withdrawal limit (`AvailableWithdrawalCredit`) debited $100. If `AvailableCreditLimit` was $1000 and `AvailableWithdrawalCredit` was $500, the `AvailableCreditLimit` would be $900 and the `AvailableWithdrawalCredit` $400 after this transaction.

# Adjust available credit limit based on transaction spending

In the following payload, the account’s available credit limit is set so the account cannot exceed their spending limit on transportation services. You can manage the account’s available credit limit based on transaction amount. In this case, the account is allowed to directly adjust the available credit limit without checking if the available credit limit has been exceeded.

* The `level` is set to `account` indicating the balance configuration is applied to an account, specifically to account `12345678`. This is the same account identified in the `impact_account` object that will have its available credit limit adjusted based on transaction amounts.
* The `configs` object is the balance configuration. The `filters` object determines the transaction filtering criteria like `processing_codes` or  merchant category codes (`mcc`). The `processing_codes` field is required. Processing code `903002` is for utilities and `mcc` `4000` is for transportation services.
* In the `result` object, the `impact` value of `AvailableCreditLimit` indicates that the platform  adjusts this limit. Since `amount` is the `contract_amount`, the amount credited to `AvailableCreditLimit` is the `contract_amount`, which is the final amount including any interest or fees.
* The value in the `impact_account.account_id` identifies the account that has its available credit limit (`AvailableCreditLimit`) adjusted.

```json
{
    "level": "account",
    "account_id": 12345678,
    "configs": [
        {
            "filters": {
                "processing_codes": [
                    "903002"
                ],
                "mcc":[
                    "4000"
                ]
            },
            "scenarios": [
                {
                    "condition": {
                        "order": 1,
                        "type": "default"
                    },
                    "result": {
                        "impact": [
                            "AvailableCreditLimit"
                        ],
                        "amount": "contract_amount",
                        "impact_account": {
                            "account_id": 89101112
                        }
                    }
                }
            ]
        }
    ]
}

```

Given a transaction for $10 that had a processing code of `903002` and an `mcc` of `4000` ,  the `89101112` account has its available credit limit (`AvailableCreditLimit`) debited by $10. If `AvailableCreditLimit` was $100, it would be $90 after this transaction.

# Configure installment purchase using installment limit

You can use this configuration to separate the customer’s installment purchases into a limit other than the main credit limit. You can apply this configuration at the organization, program, or account level for installment purchases using credit card authorizations.

The balance configuration first validates the available installment limit and only considers the available credit limit if there are insufficient funds in the available installment limit. When the customer pays the bill, the platform resets only the impacted balance at the moment of authorization.

The following payload is a sample of a purchase in installments configuration.

* The values in the `level` and `program_id` field define the program for this configuration.
* The `filters` object indicates that the configuration applies to purchases with the processing code of `00`
* The `min_installments` and `max_installments` values indicate that the configuration supports between 2 and 99 installments.
* The `custom` value in the `condition` field with the `order` of `1`  indicates the platform evaluates whether the balance specified in the `consider` field has sufficient funds to fulfill the current debit request. If the condition is met, the configuration is applied; otherwise, the platform proceeds to the next configuration indicated in the `order` field.
* The `default` value in the `condition` field with the `order` of `2` serves as a fallback. The platform applies this scenario only if no prior configurations meet their conditions.

```json
{
    "level": "program",
    "program_id": 1234567,
    "configs": [
        {
            "filters": {
                "processing_codes": [
                    "00"
                ],
            "min_installments": 2,
            "max_installments": 99
            },
            "scenarios": [
                {
                    "condition": {
                        "order": 1,
                        "type": "custom",
                        "amount_to_check_balance": "amount"
                    },
                    "result": {
                        "impact": [
                            "AvailableTotalInstallmentCredit"
                        ],
                        "consider": [
                            "AvailableTotalInstallmentCredit"
                        ],
                        "amount": "contract_amount",
                        "reset_limit": "payment"
                    }
                },
                {
                    "condition": {
                        "order": 2,
                        "type": "default"
                    },
                    "result": {
                        "impact": [
                            "AvailableCreditLimit"
                        ],
                        "consider": [
                            "AvailableCreditLimit",
                            "OverLimit"
                        ],
                        "amount": "contract_amount",
                        "reset_limit": "payment"
                    }
                }
            ]
        }
    ]
}
```

In this use case, a bank provides a customer with two distinct credit limits under the same account.

* Primary limit `AvailableCreditLimit` of $1000 is used for everyday purchases.
* Installment limit `AvailableTotalInstallmentCredit` of $500 is reserved specifically for purchases made in multiple installments.

When a customer initiates a purchase with multiple installments, the balance configuration first checks the installment limit. If sufficient funds are available in the installment limit, the transaction is debited from the installment limit and the primary limit remains unchanged. If the funds are not available in the installment limit, the transaction is debited from the primary limit and the installment limit is not impacted.

* If there is a $100 purchase with 5 installments that has a processing code of `00`, the platform evaluates the limits for the account that belongs to the `1234567` program. Since the account's installment limit (`AvailableTotalInstallmentCredit`) is $500 and there are sufficient funds in it for this purchase, the platform debits `AvailableTotalInstallmentCredit` by $100, making it $400 after this transaction.
* If there is a $600 purchase with 5 installments that has a processing code of `00`,  the platform evaluates the limits for the account that belongs to the `1234567` program. Since $600 is larger than the `AvailableTotalInstallmentCredit` of 500, the platform doesn't impact the `AvailableTotalInstallmentCredit`. The platform debits `AvailableCreditLimit` by $600, making it $400 after this transaction.

# Manage credit limits based on number of installments

The Pismo platform provides customizable credit limits such as personal loans. In the following example, Pismo handles credit limit impacts based on the number of installments.

Scenario A - authorizations up to 12 Installments:

* Condition 1: If authorizations have up to 12 installments and there is sufficient available credit, the platform impacts the `AvailableCreditLimit`.
* Condition 2: If the available credit is insufficient, the platform impacts the `InstallmentCreditLimit`.

Scenario B - authorizations with more than 12 Installments:

* Condition 1: For authorizations with more than 12 installments and if there is sufficient installment credit, the platform  directly impacts the `InstallmentCreditLimit`.
* Condition 2: If the `InstallmentCreditLimit` is insufficient, the platform impacts the `AvailableCreditLimit`.

To perform these configurations, create two distinct `scenarios`, each containing two specific `conditions`, as follows.

```json
{
    "level": "program",
    "program_id":   1065,
    "configs": [
        {
            "filters": {
                "processing_codes": [
                    "00"
                ],
                "min_installments": 1,
                "max_installments": 12
            },
            "scenarios": [
                {
                    "condition": {
                        "order": 1,
                        "type": "custom",
                        "amount_to_check_balance": "amount"
                    },
                    "result": {
                        "impact": [
                            "AvailableCreditLimit"
                        ],
                        "consider": [
                            "AvailableCreditLimit",
                            "OverLimit"
                        ],
                        "amount": "contract_amount",
                        "amount_consider": "principal_amount",
                        "reset_limit": "payment"
                    }
                },
                {
                    "condition": {
                        "order": 2,
                        "type": "default"
                    },
                    "result": {
                        "impact": [
                            "AvailableTotalInstallmentCredit"
                        ],
                        "amount": "contract_amount",
                        "amount_consider": "principal_amount",
                        "reset_limit": "payment"
                    }
                }
            ]
        },
        {        
            "filters": {
                "processing_codes": [
                    "00"
                ],
                "min_installments": 13,
                "max_installments": 99
            },
            "scenarios": [
                {
                    "condition": {
                        "order": 1,
                        "type": "custom",
                        "amount_to_check_balance": "amount"
                    },
                    "result": {
                        "impact": [
                            "AvailableTotalInstallmentCredit"
                        ],
                        "consider": [
                            "AvailableTotalInstallmentCredit"
                        ],
                        "amount": "contract_amount",
                        "amount_consider": "principal_amount",
                        "reset_limit": "payment"
                    }
                },
                {
                    "condition": {
                        "order": 2,
                        "type": "default"
                    },
                    "result": {
                        "impact": [
                            "AvailableCreditLimit"
                        ],
                        "amount": "contract_amount",
                        "amount_consider": "principal_amount",
                        "reset_limit": "payment"
                    }
                }
            ]
        }
    ]
}

```

In this use case, the `AvailableCreditLimit` is $1000 and `AvailableTotalInstallmentCredit` is $500.

* If there is a $100 purchase with 5 installments that has a processing code of `00`, the account that belongs to the `1234567` program has its `AvailableCreditLimit` debited by $100. If `AvailableCreditLimit` was $1000, the `AvailableTotalInstallmentCredit` would be $900 after this transaction.
* If there is a $100 purchase with 16 installments that has a processing code of `00`, the account that belongs to the `1234567` program has its installment limit (`AvailableTotalInstallmentCredit`) debited by $100. If `AvailableTotalInstallmentCredit` was $500, the `AvailableTotalInstallmentCredit` would be $400 after this transaction.
* If there is a $600 purchase with 16 installments that has a processing code of `00`, the account that belongs to the `123456` program has its `AvailableCreditLimit` debited by $600. If `AvailableCreditLimit` was $1000, the `AvailableCreditLimit` would be $400 after this transaction.

# Related topics

* [Balance configurations overview](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview)
* [Balance configurations in Control Center](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center)
* [Balance configurations API](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config-1)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.


### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `post-v1-balances-config-1` | API; Balance configurations API; Create balance configuration; balance configuration | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Lifecycle status

- `docs/core-platform/balance-configuration-use-cases.md`: updatedAt 2026-03-18T15:14:37.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Operation link `post-v1-balances-config-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/balance-configuration-use-cases.md` | whole document | https://developers.pismo.io/pismo-docs/docs/balance-configuration-use-cases | `c65147305d770c58…` | 2026-03-18T15:14:37.000Z |

## Related knowledge units

- `KU-CC-balance-configurations` — Control Center balance configurations
- `KU-CORE-balance-configurations` — Balance configurations and filter templates
