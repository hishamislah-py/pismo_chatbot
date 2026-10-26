---
ku_id: KU-EVT-confluent-event-config-tutorial
title: Confluent event configuration tutorial
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/confluent-event-config-tutorial.md
  sha256: 4fd3005b2a448452ec61b1a31672205778f24ed895a25ee92b57143514c750f6
  url: https://developers.pismo.io/pismo-docs/docs/confluent-event-config-tutorial
  role: primary_guide
  updated_at: '2026-08-06T12:59:32.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# Confluent event configuration tutorial

**KU ID:** `KU-EVT-confluent-event-config-tutorial` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/confluent-event-config-tutorial.md`:

> This article steps you through you through configuring Confluent Cloud for Pismo real-time event delivery via Kafka. The configuration process involves two things in Confluent Cloud:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/confluent-event-config-tutorial.md`: Confluent event configuration tutorial; 1: Create a Kafka topic; 2: Create an API key; 3: Securely share the API secret; 4: Open a service desk ticket; CLI alternative: Steps via Confluent CLI; Validate integration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/confluent-event-config-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/confluent-event-config-tutorial · updatedAt: 2026-08-06T12:59:32.000Z

<!-- source:begin path=docs/data-and-reporting/confluent-event-config-tutorial.md part=0-end -->

# Confluent event configuration tutorial

This article steps you through you through configuring Confluent Cloud for Pismo real-time event delivery via Kafka. The configuration process involves two things in Confluent Cloud:

1. **Kafka Topic** — Where Pismo produces events
2. **API Key + Secret**— Credentials for Pismo to authenticate

**Prerequisites:**

* A [Confluent Cloud account](https://docs.confluent.io/cloud/current/overview.html)
* Your Pismo Org ID (tenant ID)

## 1: Create a Kafka topic

1. Log in to **Confluent Cloud**.
2. Navigate to your cluster (or create one).
3. Click **Topics > Create topic**.
4. Enter a topic name and configure partitions.
5. Click **Create with defaults** (or customize).

## 2: Create an API key

1. Go to **API keys > Create key**.
2. Assign **WRITE + ALLOW** permissions for the topic.
3. Note the **API Key** and **API Secret**.

## 3: Securely share the API secret

<Callout icon="⚠️" theme="warn">
  **Do not paste the API Secret directly in the Jira ticket.** This is a security violation.
</Callout>

Follow these steps to securely share the API secret:

1. Create a plain .txt file containing **only the API Secret** (no extra text, no spaces).

2. Name it something descriptive (for example, confluent-api-secret.txt).

3. Place it in the **root** of your file integration bucket (the S3 bucket or SFTP configured with Pismo)

4. In the ticket template below, enter the **exact file name** (case-sensitive).

Pismo's automated routine will read the file, store the secret in a secure vault, and delete the file.

<Callout icon="⚠️" theme="warn">
  **Retry and retention policy:** To ensure ecosystem stability, the Pismo platform applies retry limits. Events that exceed the retry threshold are moved to controlled retention and can be redelivered upon request, as long as they are within the **24-hour retention window.**
</Callout>

## 4: Open a service desk ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)

2. Click **Settings**

3. Enter a short description of the incident you are reporting in the **Summary** field.

4. For **Category**, select **Data**   .

5. For **Sub-Category**, select **Event Integration**.

6. Copy the template below into the **Description** field and fill in your values:

```shell
INTEGRATION REQUEST — Confluent Cloud / Kafka (Real-Time Events)
================================================================

Org ID:              TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:         Production / Sandbox
Requester Name:      Your Name
Contact Email:       you@company.com

Kafka Topic Name:    pismo-events
Bootstrap Server:    pkc-xxxxx.us-east-1.aws.confluent.cloud:9092
API Key:             ABCDE12345FGHIJ67890
Token File Name:     confluent-api-secret.txt
  (API Secret is stored in this .txt file in the root of your
   file integration bucket — DO NOT paste the secret here)

```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. For **Priority**, select a priority level.
9. For **Environment**, select the environment for the configuration.
10. Click **Send** to submit the request.

<Callout icon="📘" theme="info">
  The bootstrap server URL is found in **Confluent Cloud > Cluster > Settings > Endpoints**.
</Callout>

<Callout icon="⏱️" theme="default">
  **Important:** After Pismo completes the initial configuration, you have 24 hours to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration pauses and you need to open a new ticket to resume.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** You can obtain information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

## CLI alternative: Steps via Confluent CLI

```shell
# Log in
confluent login

# List environments and select one
confluent environment list
confluent environment use <env-id>

# List clusters and select one
confluent kafka cluster list
confluent kafka cluster use <cluster-id>

# Step 1 — Create topic
confluent kafka topic create pismo-events --partitions 6

# Step 2 — Create API key
confluent api-key create --resource <cluster-id> --description "Pismo Data Platform"
# ⚠️ Note the API Key and Secret from the output
# Store the Secret in a .txt file — never paste in tickets

# Verify topic and key
confluent kafka topic list
confluent api-key list --resource <cluster-id>

```

**Get the bootstrap server:**

```shell
confluent kafka cluster describe --output json | jq -r '.endpoint'
# Or in Confluent Cloud Console → Cluster → Settings → Endpoints
```

## Validate integration

Run this diagnostic script to validate your integration. It checks all configuration steps and provides troubleshooting guidance:

````shell
#!/bin/bash
# ============================================================
#  Confluent Cloud Troubleshooting — Pismo Data Platform
# ============================================================
TOPIC="pismo-events"                                              # ← replace
BOOTSTRAP="pkc-xxxxx.us-east-1.aws.confluent.cloud:9092"         # ← replace
PASS=0; FAIL=0

echo "============================================================"
echo "  Confluent Cloud Integration Diagnostics"
echo "============================================================"

# 1. Confluent CLI authenticated?
echo "[1/5] Checking Confluent CLI..."
if confluent kafka cluster list >/dev/null 2>&1; then
    echo "  ✅ PASS — Authenticated and cluster accessible"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Not authenticated or no cluster selected"
    echo "  → confluent login && confluent environment use <env> && confluent kafka cluster use <cluster>"
    FAIL=$((FAIL+1))
fi

# 2. Topic exists?
echo "[2/5] Checking topic..."
if confluent kafka topic describe "$TOPIC" >/dev/null 2>&1; then
    echo "  ✅ PASS — Topic $TOPIC exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Topic $TOPIC not found"
    echo "  → confluent kafka topic create $TOPIC --partitions 6"
    FAIL=$((FAIL+1))
fi

# 3. Bootstrap server reachable?
echo "[3/5] Testing connectivity to bootstrap server..."
HOST=$(echo "$BOOTSTRAP" | cut -d: -f1)
PORT=$(echo "$BOOTSTRAP" | cut -d: -f2)
if nc -z -w 5 "$HOST" "$PORT" 2>/dev/null; then
    echo "  ✅ PASS — $BOOTSTRAP reachable"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Cannot reach $BOOTSTRAP"
    echo "  → Check firewall/VPN allows outbound port $PORT"
    FAIL=$((FAIL+1))
fi

# 4. API keys exist?
echo "[4/5] Checking API keys..."
KEY_COUNT=$(confluent api-key list --output json 2>/dev/null | jq 'length' 2>/dev/null)
if [ -n "$KEY_COUNT" ] && [ "$KEY_COUNT" -gt 0 ]; then
    echo "  ✅ PASS — $KEY_COUNT API key(s) found"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — No API keys found"
    echo "  → confluent api-key create --resource <cluster-id>"
    FAIL=$((FAIL+1))
fi

# 5. Token file uploaded?
echo "[5/5] Checking token file..."
echo "  ⚠️  MANUAL CHECK — Verify that the .txt file with the API Secret"
echo "     was placed in the root of your file integration bucket."
echo "     Pismo's automation reads and deletes it within minutes."

# Save diagnostic output to log file
LOG_FILE="/tmp/pismo-diagnostic-$(date +%Y%m%d-%H%M%S).log"

# Capture everything to log file
{
    echo "=================================================================="
    echo "  PISMO DATA PLATFORM — DIAGNOSTIC LOG"
    echo "=================================================================="
    echo ""
    echo "Timestamp: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
    echo "Integration Type: Confluent Cloud Kafka"
    echo ""
    echo "=== CONFIGURATION ==="
    echo "Org ID: $ORG_ID"
    echo "Bootstrap Server: $BOOTSTRAP_SERVER"
    echo "Cluster ID: $CLUSTER_ID"
    echo "Topic: $TOPIC_NAME"
    echo "API Key: ${API_KEY:0:8}... (truncated for security)"
    echo ""
    echo "=== TEST RESULTS ==="
    echo "Passed: $PASS"
    echo "Failed: $FAIL"
    # Note: We don't capture secrets
    echo ""
    echo "=== SECURITY NOTE ==="
    echo "API Secret is NOT captured in this log for security reasons."
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
    echo "    • Kafka Producer component (API key authentication)"
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
echo "  │  ⚠️  DO NOT share your API Secret in the ticket"
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

- `docs/data-and-reporting/confluent-event-config-tutorial.md`: updatedAt 2026-08-06T12:59:32.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/confluent-event-config-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/confluent-event-config-tutorial | `4fd3005b2a448452…` | 2026-08-06T12:59:32.000Z |

## Related knowledge units

- None.
