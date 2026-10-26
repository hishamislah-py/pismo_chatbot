---
ku_id: KU-EVT-aws-eventbridge-event-configuration-tutorial
title: AWS EventBridge event configuration tutorial
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/aws-eventbridge-event-configuration-tutorial.md
  sha256: 2dafb6d3895afd0f4169234ec4c530a42ad48d4a01dfcac178adf511f30038c8
  url: https://developers.pismo.io/pismo-docs/docs/aws-eventbridge-event-configuration-tutorial
  role: primary_guide
  updated_at: '2026-07-20T19:18:43.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# AWS EventBridge event configuration tutorial

**KU ID:** `KU-EVT-aws-eventbridge-event-configuration-tutorial` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/aws-eventbridge-event-configuration-tutorial.md`:

> Use this guide to configure AWS EventBridge to receive Pismo real‑time events. It creates two components:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/aws-eventbridge-event-configuration-tutorial.md`: AWS EventBridge event configuration tutorial; Step 1: Create the EventBridge bus; Step 2: Create an IAM policy; Step 3: Create the IAM role; Step 4: Open a Service Desk ticket; Step 5: Complete the configuration; CLI alternative: All steps via AWS CLI; Validate integration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/aws-eventbridge-event-configuration-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/aws-eventbridge-event-configuration-tutorial · updatedAt: 2026-07-20T19:18:43.000Z

<!-- source:begin path=docs/data-and-reporting/aws-eventbridge-event-configuration-tutorial.md part=0-end -->

# AWS EventBridge event configuration tutorial

Use this guide to configure AWS EventBridge to receive Pismo real‑time events. It creates two components:

1. **EventBridge Bus** — A pipeline that receives events
2. **IAM Role**— Role that grants Pismo permission to put events on your bus

**Prerequisites**:

* An AWS account
* Your Pismo Org ID (tenant ID)

## Step 1: Create the EventBridge bus

1. Log in to AWS and go to **EventBridge** (search EventBridge).

2. Click **Event buses**, then click **Create event bus**.

<Image align="center" alt="Screen capture of the Create event bus section. " border={true} src="https://files.readme.io/561328d-Screenshot_2023-04-06_at_14.04.38.png" className="border" />

3. In the **Name** field, enter a name for the bus that receives Pismo events, and then click **Create**.
4. Note the value in the **Amazon Resource Name (ARN)** field. You'll need it for the ticket.

<Image align="center" alt="Screen capture of Amazon Resource Name (ARN) field." border={true} src="https://files.readme.io/c6f2943-Screenshot_2023-04-06_at_14.06.34.png" className="border" />

## Step 2: Create an IAM policy

A policy is an entity attached to an identity or resource that determines what the identity is allowed to do in AWS.

1. Go to **IAM** > **Policies**, then select**Create policy**.

<Image align="center" alt="Screen capture of Create policy dialog." border={true} src="https://files.readme.io/dc599e5-Screenshot_2023-04-06_at_14.08.50.png" className="border" />

2. Click the **JSON** tab and enter the following code to define the policy:

```Text JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["events:PutEvents"],
            "Resource": ["arn:aws:events:<region>:<account-id>:event-bus/<bus-name>"]
        }
    ]
}
```

3. Click **Next:Tags**.

<Image align="center" alt="Screen capture of the Next Tags button." border={true} src="https://files.readme.io/059426b-1eb0465-Screenshot_2023-04-06_at_14.11.31.png" className="border" />

4. Click the **Next:Review** button and then enter a policy name.
5. Enter a policy name and click **Create policy**.

## Step 3: Create the IAM role

1. Go to **IAM** > **Roles**.

2. Click **Create role**.

<Image align="center" alt="Screen capture of the IAM dashboard." border={true} src="https://files.readme.io/ef5dee4-img_08.png" className="border" />

4. Select **AWS account** and then click **Next**.

<Image align="center" alt="Screen capture of the Select trusted entity screen." border={true} src="https://files.readme.io/61e1019-img_05.png" className="border" />

5. Select the check box for the policy you just created and then click **Next**.

<Image align="center" alt="Screen capture of the Add permissions area." border={true} src="https://files.readme.io/4c1032e-img_06.png" className="border" />

6. Enter a name for your role and then click **Create role**.

<Image align="center" alt="Screen capture of the Create role area." border={true} src="https://files.readme.io/d1ce7ce-img_04.png" className="border" />

7. Note the **IAM Role ARN**.

<Callout icon="⚠️" theme="warn">
  **Retry and retention policy:** To ensure ecosystem stability, the platform applies retry limits. Events that exceed the retry threshold are moved to controlled retention and can be redelivered upon request, as long as they are within the **24-hour retention window**.
</Callout>

## Step 4: Open a Service Desk ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)
2. Click **Settings**.
3. Enter a short description of the incident you are reporting in the **Summary** field.
4. In **Category**, select **Data**.
5. In **Sub-Category**, select **Event Integration**.
6. Copy the template below into the **Description** field, and fill in your values:

```
INTEGRATION REQUEST — AWS EventBridge (Real-Time Events)
=========================================================

Org ID:               TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:          Production / Sandbox
Requester Name:       Your Name
Contact Email:        you@company.com

AWS Account ID:       123456789012
EventBridge Bus ARN:  arn:aws:events:<region>:<account-id>:event-bus/<bus-name>
IAM Role ARN:         arn:aws:iam::<account-id>:role/<role-name>
```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. In **Priority**, select a priority level.
9. In **Environment**, select the environment for which you want the configuration.
10. Click **Send** to submit the request.

<Callout icon="📘" theme="info">
  The Org ID must be lowercase (for example, TN-a1db4e4e-315f-4a67-9036-ecacd370b561).
</Callout>

<Callout icon="⏱️" theme="default">
  **Important:** After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration will be paused and you will need to open a new ticket to resume.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

## Step 5: Complete the configuration

After Pismo processes your ticket, you'll receive an **external ID** and **Pismo's AWS account ID**. Then:

1. Go to **IAM > Roles**.
2. Select your role.
3. Select **Trust Relationships > Edit trust policy**.
4. Replace the existing trust policy with the following text, using the values provided by Pismo. This trust policy allows Pismo to assume your IAM role and access the SNS topic on your behalf. The `sts:ExternalId` condition adds an additional security layer by ensuring only requests containing the external ID provided by Pismo can assume the role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<PISMO_AWS_ACCOUNT_ID>:role/dataplatform-lambda-fn-<YOUR_ORG_ID>"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "<PISMO_PROVIDED_EXTERNAL_ID>"
                }
            }
        }
    ]
}
```

<Callout icon="📘" theme="info">
  The Org ID value must use lowercase letters.
</Callout>

5. Click **Update policy**. Events will start flowing to your EventBridge bus.

## CLI alternative: All steps via AWS CLI

The following AWS CLI commands perform the same configuration described previously in Steps 1 through 5. Replace the example values with your own environment settings and run the commands in order.

```
# Variables — replace with your values
BUS_NAME="pismo-event-bus"
POLICY_NAME="pismo-eventbridge-put"
ROLE_NAME="pismo-eventbridge-role"
REGION="us-east-1"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Step 1 — Create EventBridge bus
aws events create-event-bus --name "$BUS_NAME" --region "$REGION"

BUS_ARN="arn:aws:events:${REGION}:${ACCOUNT_ID}:event-bus/${BUS_NAME}"

# Step 2 — Create the IAM policy
cat > /tmp/pismo-eb-policy.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["events:PutEvents"],
            "Resource": ["$BUS_ARN"]
        }
    ]
}
EOF

aws iam create-policy \
    --policy-name "$POLICY_NAME" \
    --policy-document file:///tmp/pismo-eb-policy.json

POLICY_ARN="arn:aws:iam::${ACCOUNT_ID}:policy/${POLICY_NAME}"

# Step 3 — Create the IAM role
cat > /tmp/pismo-eb-trust.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": { "AWS": "${ACCOUNT_ID}" },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF

aws iam create-role \
    --role-name "$ROLE_NAME" \
    --assume-role-policy-document file:///tmp/pismo-eb-trust.json

aws iam attach-role-policy \
    --role-name "$ROLE_NAME" \
    --policy-arn "$POLICY_ARN"

ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/${ROLE_NAME}"

echo "EventBridge Bus ARN: $BUS_ARN"
echo "IAM Role ARN:        $ROLE_ARN"
echo "AWS Account ID:      $ACCOUNT_ID"
```

**Step 4: Update trust policy** (after receiving Pismo's external ID):

```
PISMO_ACCOUNT_ID="<from-pismo>"
ORG_ID="<your-org-id>"
EXTERNAL_ID="<from-pismo>"

cat > /tmp/pismo-eb-trust-final.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::${PISMO_ACCOUNT_ID}:role/dataplatform-lambda-fn-${ORG_ID}"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "${EXTERNAL_ID}"
                }
            }
        }
    ]
}
EOF

aws iam update-assume-role-policy \
    --role-name "$ROLE_NAME" \
    --policy-document file:///tmp/pismo-eb-trust-final.json

echo "Trust policy updated."
```

## Validate integration

Run this diagnostic script to validate your integration. It checks all configuration steps and provides troubleshooting guidance:

````
#!/bin/bash
# ============================================================
#  AWS EventBridge Troubleshooting — Pismo Data Platform
# ============================================================
BUS_NAME="pismo-event-bus"        # ← replace
ROLE_NAME="pismo-eventbridge-role" # ← replace
REGION="us-east-1"                 # ← replace
PASS=0; FAIL=0

echo "============================================================"
echo "  AWS EventBridge Integration Diagnostics"
echo "============================================================"

# 1. AWS CLI configured?
echo "[1/5] Checking AWS CLI..."
if aws sts get-caller-identity >/dev/null 2>&1; then
    ACCT=$(aws sts get-caller-identity --query Account --output text)
    echo "  ✅ PASS — Account $ACCT"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — AWS CLI not configured"; FAIL=$((FAIL+1))
fi

# 2. Event bus exists?
echo "[2/5] Checking event bus..."
if aws events describe-event-bus --name "$BUS_NAME" --region "$REGION" >/dev/null 2>&1; then
    echo "  ✅ PASS — Bus exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Bus not found: $BUS_NAME"
    echo "  → aws events create-event-bus --name $BUS_NAME --region $REGION"
    FAIL=$((FAIL+1))
fi

# 3. IAM role exists?
echo "[3/5] Checking IAM role..."
if aws iam get-role --role-name "$ROLE_NAME" >/dev/null 2>&1; then
    echo "  ✅ PASS — Role exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Role not found: $ROLE_NAME"; FAIL=$((FAIL+1))
fi

# 4. Trust policy has Pismo?
echo "[4/5] Checking trust policy..."
TRUST=$(aws iam get-role --role-name "$ROLE_NAME" \
    --query 'Role.AssumeRolePolicyDocument' --output json 2>/dev/null)
if echo "$TRUST" | grep -q "dataplatform-lambda-fn"; then
    echo "  ✅ PASS — Trust policy references Pismo"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Trust policy does NOT reference Pismo"
    echo "  → Update trust policy per Step 5"
    FAIL=$((FAIL+1))
fi

# 5. Test put-events
echo "[5/5] Test-putting event..."
RESULT=$(aws events put-events --region "$REGION" --entries '[{
    "Source": "pismo.diagnostic",
    "DetailType": "troubleshoot",
    "Detail": "{\"test\": true}",
    "EventBusName": "'"$BUS_NAME"'"
}]' --query 'FailedEntryCount' --output text 2>/dev/null)
if [ "$RESULT" = "0" ]; then
    echo "  ✅ PASS — Event accepted"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — PutEvents failed (FailedEntryCount=$RESULT)"
    FAIL=$((FAIL+1))
fi

# Save diagnostic output to log file
LOG_FILE="/tmp/pismo-diagnostic-$(date +%Y%m%d-%H%M%S).log"

# Capture everything to log file
{
    echo "=================================================================="
    echo "  PISMO DATA PLATFORM — DIAGNOSTIC LOG"
    echo "=================================================================="
    echo ""
    echo "Timestamp: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
    echo "Integration Type: AWS EventBridge Real-Time Events"
    echo ""
    echo "=== CONFIGURATION ==="
    echo "Org ID: $ORG_ID"
    echo "Event Bus ARN: $EVENT_BUS_ARN"
    echo "IAM Role: $ROLE_NAME"
    echo "Region: $REGION"
    echo "AWS Account: $(aws sts get-caller-identity --query Account --output text 2>/dev/null || echo 'N/A')"
    echo ""
    echo "=== TEST RESULTS ==="
    echo "Passed: $PASS"
    echo "Failed: $FAIL"
    echo ""
    echo "=== EVENT BUS POLICY ==="
    aws events describe-event-bus --name "${EVENT_BUS_ARN##*/}" --query 'Policy' --output text 2>/dev/null || echo "Could not retrieve"
} > "$LOG_FILE" 2>&1

# Display results summary
echo ""
echo "============================================================"
echo "  RESULTS: $PASS passed, $FAIL failed"
echo "============================================================"

if [ $FAIL -eq 0 ]; then
    echo ""
    echo "  ✅ All checks passed — your infrastructure is correctly configured."
    echo ""
    echo "  If events are still not arriving, there may be a potential issue in:"
    echo "    • EventBridge Publisher component (cross-account PutEvents)"
    echo "    • Event Router configuration (org/destination mapping)"
    echo "    • Event generation (no events for your org in the selected period)"
    echo ""
else
    echo ""
    echo "  ❌ Some checks failed — review the errors above."
    echo ""
    echo "  These failures indicate configuration issues in your infrastructure."
    echo "  Follow the suggested fixes (→) for each failed check."
    echo "  After fixing, run this script again to verify."
    echo ""
fi

echo "============================================================"
echo "  📋 SUPPORT TICKET INSTRUCTIONS"
echo "============================================================"
echo ""
echo "  Diagnostic log saved to: $LOG_FILE"
echo ""
echo "  To open a support ticket:"
echo "  ┌─────────────────────────────────────────────────────────┐"
echo "  │  1. Portal: https://pismolabs.atlassian.net/servicedesk │"
echo "  │     /customer/portal/10                                 │"
echo "  │  2. Category: Settings → Data → Event Integration"
echo "  │  3. Attach the log file OR paste its content below      │"
echo "  └─────────────────────────────────────────────────────────┘"
echo ""
echo "  Copy to clipboard (macOS):  cat $LOG_FILE | pbcopy"
echo "  Copy to clipboard (Linux):  cat $LOG_FILE | xclip -selection clipboard"
echo ""
echo "  ────────────── LOG FILE CONTENT ──────────────"
echo ""
cat "$LOG_FILE"
echo ""
echo "  ──────────────────────────────────────────────"
echo ""```
````
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/aws-eventbridge-event-configuration-tutorial.md`: updatedAt 2026-07-20T19:18:43.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/aws-eventbridge-event-configuration-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/aws-eventbridge-event-configuration-tutorial | `2dafb6d3895afd0f…` | 2026-07-20T19:18:43.000Z |

## Related knowledge units

- None.
