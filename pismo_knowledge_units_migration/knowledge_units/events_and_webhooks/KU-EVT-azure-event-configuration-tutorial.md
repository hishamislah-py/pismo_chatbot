---
ku_id: KU-EVT-azure-event-configuration-tutorial
title: Azure event configuration tutorial
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/azure-event-configuration-tutorial.md
  sha256: ee38f4c1d0d35d2c700aa1aee3d3d2723f1db67e910df157e02462ab62b52964
  url: https://developers.pismo.io/pismo-docs/docs/azure-event-configuration-tutorial
  role: primary_guide
  updated_at: '2026-07-20T19:54:22.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# Azure event configuration tutorial

**KU ID:** `KU-EVT-azure-event-configuration-tutorial` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/azure-event-configuration-tutorial.md`:

> Use this guide to configure Azure for Pismo real-time event delivery via Service Bus. You'll create two things:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/azure-event-configuration-tutorial.md`: Azure event configuration tutorial; Step 1: Create the service bus namespace; Step 2: Create the service bus topic; Step 3: Open a service desk ticket; Step 4: Grant Pismo access; CLI Alternative: All Steps via Azure CLI; Validate Integration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/azure-event-configuration-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/azure-event-configuration-tutorial · updatedAt: 2026-07-20T19:54:22.000Z

<!-- source:begin path=docs/data-and-reporting/azure-event-configuration-tutorial.md part=0-end -->

# Azure event configuration tutorial

Use this guide to configure Azure for Pismo real-time event delivery via Service Bus. You'll create two things:

1. **Service Bus Namespace** — Container for messaging components
2. **Service Bus Topic** — Where Pismo publishes events

**Prerequisites:**

* An Azure account

* Your Pismo Org ID (tenant ID)

> ⚠️ About Microsoft service bus tiers
>
> Microsoft offers guaranteed latency and throughput only when using the <Anchor label="Azure Service Bus Premium messaging tier" target="_blank" href="https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-premium-messaging">Azure Service Bus Premium messaging tier</Anchor>. The Standard tier does not offer these guarantees because it shares resources with other tenants, so its performance can vary. **If your application has low-latency requirements, the Standard messaging tier is not recommended**. Choose Premium for production workloads with SLA requirements.

## Step 1: Create the service bus namespace

1. Log in to the **Azure Portal**.

2. Search for **Service Bus**, then click **Create**.

3. Enter the subscription, resource group, namespace name, location, and pricing tier.

4. Click **Review + create**, then click **Create**.

## Step 2: Create the service bus topic

1. Navigate to your Service Bus namespace.

2. Click **Topics** > **+ Topic**.

3. Enter a name and click **Create**.

4. Note the **Topic URL** from the topic's properties. Use this format:\
   `https://<namespace>.servicebus.windows.net/<topic-name>`

<Callout icon="⚠️" theme="warn">
  Retry and retention policy: To ensure ecosystem stability, the platform applies retry limits. Events that exceed the retry threshold are moved to controlled retention and can be redelivered upon request, as long as they are within the **24-hour retention window**.
</Callout>

## Step 3: Open a service desk ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)
2. Click **Settings**.
3. Enter a short description of the incident you are reporting in the **Summary** field.
4. In **Category**, select **Data**.
5. In **Sub-Category**, select **Event Integration**.
6. Copy the template below into the **Description** field, fill in your values, and submit:

```
INTEGRATION REQUEST — Azure Service Bus (Real-Time Events)
===========================================================



Org ID:                TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:           Production / Sandbox
Requester Name:        Your Name
Contact Email:         you@company.com

Azure Tenant ID:       a1b2c3d4-e5f6-7890-abcd-ef1234567890
Service Bus Topic URL: https://<namespace>.servicebus.windows.net/<topic-name>
```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. In **Priority**, select a priority level.
9. In **Environment**, select the environment for which you want the configuration.
10. Click **Send** to submit the request.

<Callout icon="📘" theme="info">
  Find the Tenant ID in **Azure Portal** > **Microsoft Entra ID** > **Overview** > **Tenant ID**.  The Topic URL must be the full URL including the topic name (not just the namespace).
</Callout>

<Callout icon="⏱️" theme="default">
  **Important:** After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration will be paused and you will need to open a new ticket to resume.
</Callout>

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

## Step 4: Grant Pismo access

After Pismo processes your ticket, you'll receive a **Service Principal ID**. Then:

1. Navigate to your Service Bus topic.

2. Click **Access control (IAM)** > **Add role assignment**.

3. Select the **Azure Service Bus Data Sender** role.

4. Assign access to the Service Principal ID provided by Pismo.

5. Click **Save**. Events will start flowing to your Service Bus topic.

<Callout icon="📘" theme="info">
  Alternatively, Pismo may provide an admin consent URL to grant the necessary permissions in one click
</Callout>

## CLI Alternative: All Steps via Azure CLI

The following AWS CLI commands perform the same configuration described in Steps 1 through 4. Replace the example values with your own environment settings and run the commands in order.

```
# Variables — replace with your values
RESOURCE_GROUP="pismo-rg"
NAMESPACE="pismo-sb-ns"
TOPIC_NAME="pismo-events"
LOCATION="eastus"
SKU="Standard"  # Standard or Premium

# Step 1 — Create namespace
az servicebus namespace create \
    --name "$NAMESPACE" \
    --resource-group "$RESOURCE_GROUP" \
    --location "$LOCATION" \
    --sku "$SKU"

# Step 2 — Create topic
az servicebus topic create \
    --name "$TOPIC_NAME" \
    --namespace-name "$NAMESPACE" \
    --resource-group "$RESOURCE_GROUP"

# Get the Topic URL
TOPIC_URL="https://${NAMESPACE}.servicebus.windows.net/${TOPIC_NAME}"

# Get Tenant ID
TENANT_ID=$(az account show --query tenantId --output tsv)

echo "Azure Tenant ID:       $TENANT_ID"
echo "Service Bus Topic URL: $TOPIC_URL"
```

**Step 3 — Grant Pismo access** (after receiving the Service Principal ID):

```
PISMO_SP_ID="<service-principal-id-from-pismo>"

# Get topic resource ID
TOPIC_RESOURCE_ID=$(az servicebus topic show \
    --name "$TOPIC_NAME" \
    --namespace-name "$NAMESPACE" \
    --resource-group "$RESOURCE_GROUP" \
    --query id --output tsv)

az role assignment create \
    --assignee "$PISMO_SP_ID" \
    --role "Azure Service Bus Data Sender" \
    --scope "$TOPIC_RESOURCE_ID"

echo "Granted Data Sender to $PISMO_SP_ID"
```

## Validate Integration

Run this diagnostic script to validate your integration. It checks all configuration steps and provides troubleshooting guidance.

````
#!/bin/bash
# ============================================================
#  Azure Service Bus Troubleshooting — Pismo Data Platform
# ============================================================
NAMESPACE="pismo-sb-ns"         # ← replace
TOPIC_NAME="pismo-events"      # ← replace
RESOURCE_GROUP="pismo-rg"      # ← replace
PISMO_SP_ID=""                  # ← from Pismo
PASS=0; FAIL=0

echo "============================================================"
echo "  Azure Service Bus Integration Diagnostics"
echo "============================================================"

# 1. Azure CLI authenticated?
echo "[1/5] Checking Azure CLI..."
if az account show >/dev/null 2>&1; then
    TENANT=$(az account show --query tenantId --output tsv)
    echo "  ✅ PASS — Logged in, tenant: $TENANT"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Not authenticated"
    echo "  → Run: az login"
    FAIL=$((FAIL+1))
fi

# 2. Namespace exists?
echo "[2/5] Checking namespace..."
if az servicebus namespace show --name "$NAMESPACE" \
    --resource-group "$RESOURCE_GROUP" >/dev/null 2>&1; then
    echo "  ✅ PASS — Namespace exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Namespace not found: $NAMESPACE"
    FAIL=$((FAIL+1))
fi

# 3. Topic exists?
echo "[3/5] Checking topic..."
if az servicebus topic show --name "$TOPIC_NAME" \
    --namespace-name "$NAMESPACE" \
    --resource-group "$RESOURCE_GROUP" >/dev/null 2>&1; then
    echo "  ✅ PASS — Topic exists"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Topic not found: $TOPIC_NAME"
    FAIL=$((FAIL+1))
fi

# 4. Role assignment exists?
echo "[4/5] Checking role assignments..."
if [ -n "$PISMO_SP_ID" ]; then
    TOPIC_ID=$(az servicebus topic show --name "$TOPIC_NAME" \
        --namespace-name "$NAMESPACE" --resource-group "$RESOURCE_GROUP" \
        --query id --output tsv 2>/dev/null)
    ROLES=$(az role assignment list --assignee "$PISMO_SP_ID" \
        --scope "$TOPIC_ID" --output json 2>/dev/null)
    if echo "$ROLES" | grep -q "Data Sender"; then
        echo "  ✅ PASS — Data Sender role assigned"
        PASS=$((PASS+1))
    else
        echo "  ❌ FAIL — Data Sender role NOT assigned"
        echo "  → az role assignment create --assignee $PISMO_SP_ID \\"
        echo "      --role 'Azure Service Bus Data Sender' --scope $TOPIC_ID"
        FAIL=$((FAIL+1))
    fi
else
    echo "  ⚠️  SKIP — PISMO_SP_ID not set (waiting for Pismo response)"
fi

# 5. Connectivity test
echo "[5/5] Testing endpoint connectivity..."
if curl -s -o /dev/null -w "%{http_code}" "https://${NAMESPACE}.servicebus.windows.net/" | grep -q "401"; then
    echo "  ✅ PASS — Endpoint reachable (401 = auth required = expected)"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Cannot reach Service Bus endpoint"
    echo "  → Check DNS/firewall for https://${NAMESPACE}.servicebus.windows.net"
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
    echo "Integration Type: Azure Service Bus Real-Time Events"
    echo ""
    echo "=== CONFIGURATION ==="
    echo "Org ID: $ORG_ID"
    echo "Namespace: $NAMESPACE"
    echo "Topic: $TOPIC_NAME"
    echo "Subscription: $AZ_SUBSCRIPTION"
    echo "Resource Group: $RESOURCE_GROUP"
    echo ""
    echo "=== TEST RESULTS ==="
    echo "Passed: $PASS"
    echo "Failed: $FAIL"
    echo ""
    echo "=== NAMESPACE INFO ==="
    az servicebus namespace show --name "$NAMESPACE" --resource-group "$RESOURCE_GROUP" --output json 2>/dev/null || echo "Could not retrieve"
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
    echo "    • Service Bus Connector component (SAS authentication)"
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

- `docs/data-and-reporting/azure-event-configuration-tutorial.md`: updatedAt 2026-07-20T19:54:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/azure-event-configuration-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/azure-event-configuration-tutorial | `ee38f4c1d0d35d2c…` | 2026-07-20T19:54:22.000Z |

## Related knowledge units

- None.
