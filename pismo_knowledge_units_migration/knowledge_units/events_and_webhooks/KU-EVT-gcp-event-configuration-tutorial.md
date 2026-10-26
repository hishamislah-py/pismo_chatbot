---
ku_id: KU-EVT-gcp-event-configuration-tutorial
title: GCP event configuration tutorial
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/gcp-event-configuration-tutorial.md
  sha256: 729989bf023c682debc30c570363dd516f779c643d17c68855a3c458da640a79
  url: https://developers.pismo.io/pismo-docs/docs/gcp-event-configuration-tutorial
  role: primary_guide
  updated_at: '2026-07-20T19:20:22.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# GCP event configuration tutorial

**KU ID:** `KU-EVT-gcp-event-configuration-tutorial` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/gcp-event-configuration-tutorial.md`:

> This guide steps you through configuring GCP for Pismo real-time event delivery via Pub/Sub. You'll create two things:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/gcp-event-configuration-tutorial.md`: GCP event configuration tutorial; Step 1: Select or Create a Project; Step 2: Create a Pub/Sub Topic; Step 3: Open a Service Desk Ticket; Step 4: Grant Pismo Access; CLI Alternative: All Steps via gcloud CLI; Validate Integration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/gcp-event-configuration-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/gcp-event-configuration-tutorial · updatedAt: 2026-07-20T19:20:22.000Z

<!-- source:begin path=docs/data-and-reporting/gcp-event-configuration-tutorial.md part=0-end -->

# GCP event configuration tutorial

This guide steps you through configuring GCP for Pismo real-time event delivery via Pub/Sub. You'll create two things:

1. **GCP Project**(or use an existing one)

2. **Pub/Sub Topic** — Where Pismo publishes events

**Prerequisite:**

* A Google Cloud account

## Step 1: Select or Create a Project

1. In the Google Cloud Console, click the project dropdown to the left of the search field.

<Image align="center" alt="Screen capture of the Select a project area." border={true} src="https://files.readme.io/907c942-select-gcp-project.jpg" title="select-gcp-project.jpg" className="border" />

2. Select an existing project, or click **New Project** to create a new one. If you select an existing project, skip the next step.

3. Enter a project name and click **Create**.

## Step 2: Create a Pub/Sub Topic

1. Search for "topics" and press **Enter**.
2. Click **+ Create a topic**.
3. Enter a **Name** and click **Create Topic**.

<Image align="center" alt="Screen capture of the Create a topic screen." border={true} src="https://files.readme.io/7a08f63-create-a-topic.jpg" title="create-a-topic.jpg" className="border" />

<Callout icon="⚠️" theme="warn">
  **Retry and retention policy:** To ensure ecosystem stability, the Pismo platform applies retry limits. Events that exceed the retry threshold are moved to controlled retention and can be redelivered upon request, as long as they are within the **24-hour retention window**.
</Callout>

## Step 3: Open a Service Desk Ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)

2. Click **Settings**

3. Enter a short description of the incident you are reporting in the **Summary** field.

4. In the **Category** drop-down, select **Data**.

5. In the **Sub-Category** drop-down, select **Event Integration**.

6. Copy the template below into the **Description** field, fill in your values, and select **Send**.

```
INTEGRATION REQUEST — GCP Pub/Sub (Real-Time Events)
=====================================================

Org ID:              TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:         Production / Sandbox
Requester Name:      Your Name
Contact Email:       you@company.com

GCP Project ID:      my-project-123
Pub/Sub Topic Name:  pismo-events-topic
```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. In **Priority**, select a priority level.
9. In **Environment**, select the environment for which you want the configuration.
10. Click **Send** to submit the request.

<Callout icon="📘" theme="info">
  The Org ID must be lowercase. The Project ID is found in the GCP Console project selector (the **ID** column, not the Name).
</Callout>

<Callout icon="⏱️" theme="default">
  **Important:** After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration will be paused and you will need to open a new ticket to resume.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

## Step 4: Grant Pismo Access

After Pismo processes your ticket, you'll receive a **GCP IAM Service Account ID**. Then:

1. Navigate to your Pub/Sub topic.

2. Click the **Permissions** tab, then click **+ Add Principal**.

<Image align="center" alt="Screen capture of the permissions tab." border={true} src="https://files.readme.io/4bc495e-permissions-tab.jpg" title="permissions-tab.jpg" className="border" />

4. Enter the Service Account ID in the **New principals** field.

5. Select **Pub/Sub > Pub/Sub Publisher** from the role dropdown.

<Image align="center" alt="Screen capture of the Select a role menu." border={true} src="https://files.readme.io/1419fa2-add-principals.jpg" title="add-principals.jpg" className="border" />

6. Click **Save**. Events will start flowing to your topic.

## CLI Alternative: All Steps via gcloud CLI

```
# Variables — replace with your values
PROJECT_ID="my-project-123"
TOPIC_NAME="pismo-events-topic"

# Step 1 — Set project
gcloud config set project "$PROJECT_ID"

# Step 2 — Create Pub/Sub topic
gcloud pubsub topics create "$TOPIC_NAME"

echo "Project ID: $PROJECT_ID"
echo "Topic Name: $TOPIC_NAME"
```

**Step 3: Grant Pismo access** (after receiving the Service Account ID):

```
PISMO_SA="<service-account-id-from-pismo>@<project>.iam.gserviceaccount.com"

gcloud pubsub topics add-iam-policy-binding "$TOPIC_NAME" \
    --member="serviceAccount:${PISMO_SA}" \
    --role="roles/pubsub.publisher"

echo "Granted Pub/Sub Publisher to $PISMO_SA"
```

## Validate Integration

Run this diagnostic script to validate your integration. It checks all configuration steps and provides troubleshooting guidance:

````
#!/bin/bash
# ============================================================
#  GCP Pub/Sub Troubleshooting — Pismo Data Platform
# ============================================================
PROJECT_ID="my-project-123"                    # ← replace
TOPIC_NAME="pismo-events-topic"                # ← replace
PISMO_SA=""                                    # ← from Pismo
PASS=0; FAIL=0

echo "============================================================"
echo "  GCP Pub/Sub Integration Diagnostics"
echo "============================================================"

# 1. gcloud authenticated?
echo "[1/5] Checking gcloud auth..."
if gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>/dev/null | head -1 | grep -q "@"; then
    ACCT=$(gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>/dev/null | head -1)
    echo "  ✅ PASS — Authenticated as $ACCT"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Not authenticated"
    echo "  → Run: gcloud auth login"
    FAIL=$((FAIL+1))
fi

# 2. Project accessible?
echo "[2/5] Checking project..."
if gcloud projects describe "$PROJECT_ID" >/dev/null 2>&1; then
    echo "  ✅ PASS — Project $PROJECT_ID accessible"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Cannot access project $PROJECT_ID"
    FAIL=$((FAIL+1))
fi

# 3. Topic exists?
echo "[3/5] Checking topic..."
if gcloud pubsub topics describe "$TOPIC_NAME" --project="$PROJECT_ID" >/dev/null 2>&1; then
    echo "  ✅ PASS — Topic exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Topic not found: $TOPIC_NAME"
    echo "  → gcloud pubsub topics create $TOPIC_NAME --project=$PROJECT_ID"
    FAIL=$((FAIL+1))
fi

# 4. Pismo SA has Publisher?
echo "[4/5] Checking IAM binding..."
if [ -n "$PISMO_SA" ]; then
    IAM=$(gcloud pubsub topics get-iam-policy "$TOPIC_NAME" \
        --project="$PROJECT_ID" --format=json 2>/dev/null)
    if echo "$IAM" | grep -q "$PISMO_SA"; then
        echo "  ✅ PASS — Pismo SA has binding"
        PASS=$((PASS+1))
    else
        echo "  ❌ FAIL — Pismo SA not in IAM policy"
        echo "  → Grant: gcloud pubsub topics add-iam-policy-binding $TOPIC_NAME \\"
        echo "      --member=serviceAccount:$PISMO_SA --role=roles/pubsub.publisher"
        FAIL=$((FAIL+1))
    fi
else
    echo "  ⚠️  SKIP — PISMO_SA not set (waiting for Pismo response)"
fi

# 5. Test publish
echo "[5/5] Test-publishing..."
if gcloud pubsub topics publish "$TOPIC_NAME" --project="$PROJECT_ID" \
    --message='{"diagnostic":"pismo-troubleshoot"}' >/dev/null 2>&1; then
    echo "  ✅ PASS — Message published"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Cannot publish to topic"; FAIL=$((FAIL+1))
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
    echo "Integration Type: GCP Pub/Sub Real-Time Events"
    echo ""
    echo "=== CONFIGURATION ==="
    echo "Org ID: $ORG_ID"
    echo "Project: $PROJECT_ID"
    echo "Topic: $TOPIC_NAME"
    echo ""
    echo "=== TEST RESULTS ==="
    echo "Passed: $PASS"
    echo "Failed: $FAIL"
    echo ""
    echo "=== TOPIC IAM POLICY ==="
    gcloud pubsub topics get-iam-policy "$TOPIC_NAME" --project="$PROJECT_ID" 2>/dev/null || echo "Could not retrieve"
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
    echo "    • Pub/Sub Publisher component (service account permissions)"
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

<br />
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/gcp-event-configuration-tutorial.md`: updatedAt 2026-07-20T19:20:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/gcp-event-configuration-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/gcp-event-configuration-tutorial | `729989bf023c682d…` | 2026-07-20T19:20:22.000Z |

## Related knowledge units

- None.
