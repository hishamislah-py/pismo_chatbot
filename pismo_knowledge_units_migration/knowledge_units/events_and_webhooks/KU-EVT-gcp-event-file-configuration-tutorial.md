---
ku_id: KU-EVT-gcp-event-file-configuration-tutorial
title: GCP event file configuration tutorial
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/gcp-event-file-configuration-tutorial.md
  sha256: b7e6f8baed6ac5f08baedc72d25a0496624955a9a19db17db8fa5da4edeb4739
  url: https://developers.pismo.io/pismo-docs/docs/gcp-event-file-configuration-tutorial
  role: primary_guide
  updated_at: '2026-07-23T19:10:46.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# GCP event file configuration tutorial

**KU ID:** `KU-EVT-gcp-event-file-configuration-tutorial` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/gcp-event-file-configuration-tutorial.md`:

> This guide steps you through configuring Google Cloud Platform (GCP) for Pismo real-time event delivery via Pub/Sub. You'll create a GCP project (a container for your Google Cloud resources) and a Pub/Sub topic where Pismo publishes events.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/gcp-event-file-configuration-tutorial.md`: GCP event file configuration tutorial; Step 1: Select or create a project; Step 2: Create a Google Cloud Storage (GCS) bucket; Step 3: Open a service desk ticket; Step 4: Grant Pismo access; CLI alternative: All steps via gcloud/gsutil; Validate integration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/gcp-event-file-configuration-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/gcp-event-file-configuration-tutorial · updatedAt: 2026-07-23T19:10:46.000Z

<!-- source:begin path=docs/data-and-reporting/gcp-event-file-configuration-tutorial.md part=0-end -->

# GCP event file configuration tutorial

This guide steps you through configuring Google Cloud Platform (GCP) for Pismo real-time event delivery via Pub/Sub. You'll create a GCP project (a container for your Google Cloud resources) and a Pub/Sub topic where Pismo publishes events.

**Prerequisites:**

* A Google Cloud account

<Callout icon="⚠️" theme="warn">
  **File retention and download responsibility.** Pismo retains files in the bucket while your organization is active. However, we strongly recommend downloading files to your own infrastructure as soon as they are produced — either in real time (triggered by event notifications) or within 24 hours if you use a batch/polling strategy. These files belong to your organization, and keeping a local copy ensures you always have access. Please note that Pismo may charge additional fees for recovery requests of files older than 30 days.
</Callout>

## Step 1: Select or create a project

1. In the Google Cloud Console, click the project dropdown.

<Image align="center" alt="Screen capture of Select a project selection." border={true} src="https://files.readme.io/53653b2-907c942-select-gcp-project.jpg" title="907c942-select-gcp-project.jpg" className="border" />

2. Select an existing project, or click **New Project** to create a new one. If you select an existing project, skip the next two steps.

3. Enter a project name and click **Create**.

4. Select your project from the **Notifications** menu or from the projects dropdown menu.

## Step 2: Create a Google Cloud Storage (GCS) bucket

1. Navigate to **Cloud Storage**.

<Image align="center" alt="Screen capture of GCP Console. " border={true} src="https://files.readme.io/2bb312c-gcp_bucket.png" title="gcp bucket.png" className="border" />

2. Click **+ Create Bucket**.

<Image align="center" alt="Screen capture of the area to Name your bucket." border={true} src="https://files.readme.io/841b269-create_gcp_bucket.png" title="create_gcp_bucket.png" className="border" />

3. Enter a bucket name, then click **Create** at the bottom of the form.

<Image align="center" border={true} src="https://files.readme.io/d9d4403681956be65b74c7ba49e503f642789e7069446bc2432a3dd4fb16ed89-image.png" className="border" />

## Step 3: Open a service desk ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)
2. Click **Settings**.
3. Enter a short description of the incident you are reporting in the **Summary** field.
4. In **Category**, select **Data**.
5. In **Sub-Category**, select **File Integration**.
6. Copy the template below into the **Description** field and fill in your values:

```
INTEGRATION REQUEST — GCP Cloud Storage (Batch File Delivery)
=============================================================

Org ID:            TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:       Production / Sandbox
Requester Name:    Your Name
Contact Email:     you@company.com

GCP Project ID:    my-project-123
GCS Bucket Name:   my-pismo-data-bucket
```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. In **Priority**, select a priority level.
9. In **Environment**, select the environment for the configuration.
10. Click **Send** to submit the request.

<Callout icon="📘" theme="info">
  The Project ID is found in the GCP Console project selector — use the **ID** column (for example, my-project-123), not the display name. Bucket names must be globally unique, lowercase.
</Callout>

<Callout icon="⏱️" theme="default">
  **Important:** After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration will be paused and you will need to open a new ticket to resume.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

## Step 4: Grant Pismo access

After Pismo processes your ticket, you'll receive a **GCP IAM Service Account ID**. Then:

1. Go to your GCS bucket, select the **Permissions** tab, then click **Add**.

<Image align="center" alt="Permissions screen capture of the GCP bucket." border={true} src="https://files.readme.io/329d243-add_bucket_permission.png" title="add_bucket_permission.png" className="border" />

2. Paste the Service Account ID in the **New Principals** field.

<Image align="center" alt="Screen capture of the New Principals field. " border={true} src="https://files.readme.io/c45922c-new_principal.png" title="new_principal.png" className="border" />

3. Click in the **Select a role** field, and select **Cloud Storage** > **Storage Object Creator**.

<Image align="center" alt="Screen capture of the filter. " border={true} src="https://files.readme.io/e64e7c2-cloud_storage_object.png" title="cloud_storage_object.png" className="border" />

4. Click **Save**. Pismo will start delivering files to your bucket.

<Image align="center" alt="Screen capture showing how to save changes. " border={true} src="https://files.readme.io/db70307-save_principle.png" title="save_principle.png" className="border" />

## CLI alternative: All steps via gcloud/gsutil

```shell
# Variables — replace with your values
PROJECT_ID="my-project-123"
BUCKET_NAME="my-pismo-data-bucket"
LOCATION="us-east1"

# Step 1 — Set project
gcloud config set project "$PROJECT_ID"

# Step 2 — Create bucket
gsutil mb -p "$PROJECT_ID" -l "$LOCATION" "gs://${BUCKET_NAME}/"

echo "Project ID:      $PROJECT_ID"
echo "GCS Bucket Name: $BUCKET_NAME"
```

**Step 3**: **Grant Pismo access** (after receiving the Service Account ID):

```shell
PISMO_SA="<service-account-id-from-pismo>@<project>.iam.gserviceaccount.com"

gsutil iam ch "serviceAccount:${PISMO_SA}:objectCreator" "gs://${BUCKET_NAME}"

echo "Granted Storage Object Creator to $PISMO_SA"
```

**Download files:**

```shell
# List files in the bucket
gsutil ls "gs://${BUCKET_NAME}/main_stream/"

# Download all files
gsutil -m cp -r "gs://${BUCKET_NAME}/main_stream/*" ./downloads/

# Download a specific file
gsutil cp "gs://${BUCKET_NAME}/main_stream/FILENAME" ./downloads/
```

## Validate integration

Run this diagnostic script to validate your integration. It checks all configuration steps and provides troubleshooting guidance:

````shell
#!/bin/bash
# ============================================================
#  GCP Cloud Storage File Troubleshooting — Pismo
# ============================================================
PROJECT_ID="my-project-123"            # ← replace
BUCKET_NAME="my-pismo-data-bucket"     # ← replace
PISMO_SA=""                            # ← from Pismo
PASS=0; FAIL=0

echo "============================================================"
echo "  GCP Cloud Storage File Integration Diagnostics"
echo "============================================================"

# 1. gcloud authenticated?
echo "[1/5] Checking gcloud auth..."
if gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>/dev/null | head -1 | grep -q "@"; then
    echo "  ✅ PASS — Authenticated"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Not authenticated → gcloud auth login"
    FAIL=$((FAIL+1))
fi

# 2. Project accessible?
echo "[2/5] Checking project..."
if gcloud projects describe "$PROJECT_ID" >/dev/null 2>&1; then
    echo "  ✅ PASS — Project accessible"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Cannot access project $PROJECT_ID"
    FAIL=$((FAIL+1))
fi

# 3. Bucket exists?
echo "[3/5] Checking bucket..."
if gsutil ls -b "gs://${BUCKET_NAME}/" >/dev/null 2>&1; then
    echo "  ✅ PASS — Bucket exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Bucket not found: $BUCKET_NAME"
    echo "  → gsutil mb -p $PROJECT_ID gs://${BUCKET_NAME}/"
    FAIL=$((FAIL+1))
fi

# 4. Pismo SA has access?
echo "[4/5] Checking IAM binding..."
if [ -n "$PISMO_SA" ]; then
    IAM=$(gsutil iam get "gs://${BUCKET_NAME}" 2>/dev/null)
    if echo "$IAM" | grep -q "$PISMO_SA"; then
        echo "  ✅ PASS — Pismo SA has bucket access"
        PASS=$((PASS+1))
    else
        echo "  ❌ FAIL — Pismo SA not in bucket IAM"
        echo "  → gsutil iam ch serviceAccount:${PISMO_SA}:objectCreator gs://${BUCKET_NAME}"
        FAIL=$((FAIL+1))
    fi
else
    echo "  ⚠️  SKIP — PISMO_SA not set"
fi

# 5. Files present?
echo "[5/5] Checking for files..."
FILES=$(gsutil ls "gs://${BUCKET_NAME}/main_stream/" 2>/dev/null | head -5)
if [ -n "$FILES" ]; then
    echo "  ✅ PASS — Files found in main_stream/"
    echo "     $(echo "$FILES" | head -3)"
    PASS=$((PASS+1))
else
    echo "  ⚠️  INFO — No files yet in main_stream/"
    echo "     Files appear after events are generated"
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
    echo "Integration Type: GCP Cloud Storage File Delivery"
    echo ""
    echo "=== CONFIGURATION ==="
    echo "Org ID: $ORG_ID"
    echo "Project: $PROJECT_ID"
    echo "Bucket: $BUCKET_NAME"
    echo ""
    echo "=== TEST RESULTS ==="
    echo "Passed: $PASS"
    echo "Failed: $FAIL"
    echo ""
    echo "=== BUCKET IAM POLICY ==="
    gsutil iam get "gs://$BUCKET_NAME" 2>/dev/null || echo "Could not retrieve"
    echo ""
    echo "=== RECENT FILES (last 5) ==="
    gsutil ls -l "gs://$BUCKET_NAME/" 2>/dev/null | tail -5 || echo "Could not retrieve"
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
    echo "    • File Copier component (S3-to-GCS sync)"
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
echo ""```
````
<!-- source:end -->

## Lifecycle status

- `docs/data-and-reporting/gcp-event-file-configuration-tutorial.md`: updatedAt 2026-07-23T19:10:46.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/gcp-event-file-configuration-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/gcp-event-file-configuration-tutorial | `b7e6f8baed6ac5f0…` | 2026-07-23T19:10:46.000Z |

## Related knowledge units

- None.
