---
ku_id: KU-EVT-aws-event-file-configuration-tutorial
title: AWS event file configuration tutorial
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/aws-event-file-configuration-tutorial.md
  sha256: eb38b7aa77f93c8c2fb863df04ba0924fee863dbbf9832fd6942794d59e18fc4
  url: https://developers.pismo.io/pismo-docs/docs/aws-event-file-configuration-tutorial
  role: primary_guide
  updated_at: '2026-07-20T19:55:12.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# AWS event file configuration tutorial

**KU ID:** `KU-EVT-aws-event-file-configuration-tutorial` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/aws-event-file-configuration-tutorial.md`:

> This guide steps you through configuring AWS for Pismo batch event file delivery to an S3 bucket. You'll create:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/aws-event-file-configuration-tutorial.md`: AWS event file configuration tutorial; Step 1 — Create the IAM Policy; Step 2 — Create the IAM Role; Step 3 — Open a Service Desk Ticket; **Important:** After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration will be paused and you will need to open a new ticket to resume.; Step 4 — Complete the Configuration; CLI Alternative — All Steps via AWS CLI; Validate Integration; Diagnostic Script

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/aws-event-file-configuration-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/aws-event-file-configuration-tutorial · updatedAt: 2026-07-20T19:55:12.000Z

<!-- source:begin path=docs/data-and-reporting/aws-event-file-configuration-tutorial.md part=0-end -->

# AWS event file configuration tutorial

This guide steps you through configuring AWS for Pismo batch event file delivery to an S3 bucket. You'll create:

1. **IAM Policy** — Grants permission to assume Pismo's consumer role
2. **IAM Role** — Identity used by your routines to download files

<Callout icon="📘" theme="info">
  **Optional but recommended:** Real-time event delivery (SNS or EventBridge) can be configured to receive notifications when new files are available. If you don't have real-time delivery, you can also poll the bucket periodically (for example, daily or hourly) to check for new files.
</Callout>

**Prerequisites:**

* An AWS account
* Your Pismo Org ID (tenant ID)

<Callout icon="⚠️" theme="warn">
  **File retention and download responsibility.** Pismo retains files in the bucket while your organization is active. However, we strongly recommend downloading files to your own infrastructure as soon as they are produced — either in real time (triggered by event notifications) or within 24 hours if you use a batch/polling strategy. These files belong to your organization, and keeping a local copy ensures you always have access. Please note that Pismo may charge additional fees for recovery requests of files older than 30 days.
</Callout>

***

## Step 1 — Create the IAM Policy

1. Go to **IAM** > **Policies** > **Create policy**.
2. Click the **JSON** tab and paste:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::<PISMO_AWS_ACCOUNT_ID>:role/dataplatform-consumer-<ORG_ID>"
        }
    ]
}
```

Replace `<PISMO_AWS_ACCOUNT_ID>` and `<ORG_ID>` with values provided by Pismo after you submit the ticket.

3. Click **Next:Tags** > **Next:Review** > name the policy > **Create policy**.

## Step 2 — Create the IAM Role

1. Go to **IAM** > **Roles** > **Create role**.
2. Select **AWS account** > **Next**.
3. Select the policy you just created > **Next**.
4. Name the role > **Create role**.
5. Note the **IAM Role ARN**.

***

## Step 3 — Open a Service Desk Ticket

Go to: **[https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)**

1. Click **Settings**
2. In **Category**, select **Data**
3. In **Sub-Category**, select **File Integration**
4. Copy the template below into the **Description** field, fill in your values, and submit:

```
INTEGRATION REQUEST — AWS S3 (Batch File Delivery)
===================================================

Org ID:            TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:       Production / Sandbox
Requester Name:    Your Name
Contact Email:     you@company.com

AWS Account ID:    123456789012
IAM Role ARN:      arn:aws:iam::<account-id>:role/<role-name>

Real-time event delivery configured?  Yes / No / Will use polling instead
```

<Callout icon="⏱️" theme="default">
  ### **Important:** After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration will be paused and you will need to open a new ticket to resume.
</Callout>

> 📘 **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.

***

## Step 4 — Complete the Configuration

After Pismo processes your ticket, you'll receive:

* An **S3 bucket** ARN (dedicated to your Org)
* A **consumer IAM Role** ARN (for file downloading)

Your routine (Lambda, worker, application) should:

1. Invoke `sts:AssumeRole` on Pismo's consumer IAM Role.
2. Use the temporary credentials to download files via `s3:GetObject`.

***

## CLI Alternative — All Steps via AWS CLI

```bash
# Variables — replace with your values
POLICY_NAME="pismo-consumer-assume"
ROLE_NAME="pismo-file-consumer-role"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Step 1 — Create IAM policy (use placeholder until Pismo confirms values)
cat > /tmp/pismo-consumer-policy.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::<PISMO_AWS_ACCOUNT_ID>:role/dataplatform-consumer-<ORG_ID>"
        }
    ]
}
EOF

aws iam create-policy \
    --policy-name "$POLICY_NAME" \
    --policy-document file:///tmp/pismo-consumer-policy.json

# Step 2 — Create IAM role
cat > /tmp/pismo-consumer-trust.json <<EOF
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
    --assume-role-policy-document file:///tmp/pismo-consumer-trust.json

aws iam attach-role-policy \
    --role-name "$ROLE_NAME" \
    --policy-arn "arn:aws:iam::${ACCOUNT_ID}:policy/${POLICY_NAME}"

ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/${ROLE_NAME}"
echo "IAM Role ARN:   $ROLE_ARN"
echo "AWS Account ID: $ACCOUNT_ID"
```

**Step 4 — Download files** (after Pismo provides the consumer role and bucket):

```bash
PISMO_CONSUMER_ROLE="arn:aws:iam::<PISMO_ACCOUNT_ID>:role/dataplatform-consumer-<ORG_ID>"
PISMO_BUCKET="pismo-dataplatform-<org-id>"

# Assume the Pismo consumer role
CREDS=$(aws sts assume-role \
    --role-arn "$PISMO_CONSUMER_ROLE" \
    --role-session-name "pismo-download" \
    --query 'Credentials' --output json)

export AWS_ACCESS_KEY_ID=$(echo "$CREDS" | jq -r '.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo "$CREDS" | jq -r '.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo "$CREDS" | jq -r '.SessionToken')

# List files
aws s3 ls "s3://${PISMO_BUCKET}/main_stream/"

# Download all files
aws s3 cp "s3://${PISMO_BUCKET}/main_stream/" ./downloads/ --recursive

# Clean up temp credentials
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
```

\============================================================
RESULTS: 5 passed, 0 failed
===========================

***

## Validate Integration

Run this script to validate your integration. It checks all configuration steps and provides troubleshooting guidance:

### Diagnostic Script

```bash
#!/bin/bash
# ============================================================
#  AWS S3 File Troubleshooting — Pismo Data Platform
# ============================================================
ROLE_NAME="pismo-file-consumer-role"                                            # ← replace
PISMO_CONSUMER_ROLE="arn:aws:iam::<pismo-acct>:role/dataplatform-consumer-<id>" # ← replace
PISMO_BUCKET="pismo-dataplatform-<org-id>"                                      # ← replace
PASS=0; FAIL=0

echo "============================================================"
echo "  AWS S3 File Integration Diagnostics"
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

# 2. Local IAM role exists?
echo "[2/5] Checking local IAM role..."
if aws iam get-role --role-name "$ROLE_NAME" >/dev/null 2>&1; then
    echo "  ✅ PASS — Role exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Role $ROLE_NAME not found"; FAIL=$((FAIL+1))
fi

# 3. Policy attached?
echo "[3/5] Checking attached policies..."
POLICIES=$(aws iam list-attached-role-policies --role-name "$ROLE_NAME" \
    --query 'AttachedPolicies[].PolicyName' --output text 2>/dev/null)
if [ -n "$POLICIES" ]; then
    echo "  ✅ PASS — Policies: $POLICIES"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — No policies attached"; FAIL=$((FAIL+1))
fi

# 4. Can assume Pismo consumer role?
echo "[4/5] Testing AssumeRole..."
ASSUME=$(aws sts assume-role --role-arn "$PISMO_CONSUMER_ROLE" \
    --role-session-name "diag-test" 2>&1)
if echo "$ASSUME" | jq -e '.Credentials' >/dev/null 2>&1; then
    echo "  ✅ PASS — AssumeRole succeeded"
    PASS=$((PASS+1))

    # 5. Can list bucket?
    echo "[5/5] Listing bucket..."
    export AWS_ACCESS_KEY_ID=$(echo "$ASSUME" | jq -r '.Credentials.AccessKeyId')
    export AWS_SECRET_ACCESS_KEY=$(echo "$ASSUME" | jq -r '.Credentials.SecretAccessKey')
    export AWS_SESSION_TOKEN=$(echo "$ASSUME" | jq -r '.Credentials.SessionToken')

    if aws s3 ls "s3://${PISMO_BUCKET}/main_stream/" >/dev/null 2>&1; then
        echo "  ✅ PASS — Bucket accessible"
        PASS=$((PASS+1))
    else
        echo "  ❌ FAIL — Cannot list bucket"
        echo "  → Verify bucket name and KMS permissions"
        FAIL=$((FAIL+1))
    fi

    unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
else
    echo "  ❌ FAIL — AssumeRole failed"
    echo "  → $ASSUME"
    echo "  → Verify your IAM policy allows sts:AssumeRole on the Pismo consumer role"
    FAIL=$((FAIL+1))
    echo "[5/5] Skipped (depends on AssumeRole)"
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
    echo "Integration Type: AWS S3 File Delivery"
    echo ""
    echo "=== CONFIGURATION ==="
    echo "Org ID: $ORG_ID"
    echo "Consumer Role: $CONSUMER_ROLE"
    echo "Bucket: $BUCKET_NAME"
    echo "AWS Account: $(aws sts get-caller-identity --query Account --output text 2>/dev/null || echo 'N/A')"
    echo ""
    echo "=== TEST RESULTS ==="
    echo "Passed: $PASS"
    echo "Failed: $FAIL"
    echo ""
    echo "=== ASSUMED ROLE SESSION ==="
    echo "If assume-role worked, recent files were listed above"
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
    echo "    • File Generator component (event batching and S3 upload)"
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
echo "  │  2. Category: Settings → Data → File Integration"
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
echo ""
```
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/aws-event-file-configuration-tutorial.md`: updatedAt 2026-07-20T19:55:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/aws-event-file-configuration-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/aws-event-file-configuration-tutorial | `eb38b7aa77f93c8c…` | 2026-07-20T19:55:12.000Z |

## Related knowledge units

- None.
