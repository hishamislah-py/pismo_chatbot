---
ku_id: KU-EVT-sftp-event-file-configuration-tutorial
title: SFTP event file configuration tutorial
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/sftp-event-file-configuration-tutorial.md
  sha256: 189c63f664fbd2e2264c4b2004368c0a7e23d2d10a6f869a3751803199ebeaac
  url: https://developers.pismo.io/pismo-docs/docs/sftp-event-file-configuration-tutorial
  role: primary_guide
  updated_at: '2026-07-20T19:15:35.000Z'
operations: []
related_kus: []
grouping_rationale: single source page
---

# SFTP event file configuration tutorial

**KU ID:** `KU-EVT-sftp-event-file-configuration-tutorial` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/sftp-event-file-configuration-tutorial.md`:

> This guide steps you through using SFTP to retrieve Pismo batch event files. Pismo's SFTP service abstracts the S3 bucket behind an SFTP layer — when you connect, you access the same event files.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/sftp-event-file-configuration-tutorial.md`: SFTP event file configuration tutorial; Step 1: Generate an SSH RSA Key Pair; Option A: Command Line (Linux / macOS / Windows with Git Bash); Option B: PuTTYgen (Windows GUI); Step 2: Open a Service Desk Ticket; CLI: Find your public IP to include in the template:; Step 3: Connect; CLI connection:; GUI connection (FileZilla):; Step 4: Download Files; Knowing When Files Are Available; Validate Integration

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/sftp-event-file-configuration-tutorial.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/sftp-event-file-configuration-tutorial · updatedAt: 2026-07-20T19:15:35.000Z

<!-- source:begin path=docs/data-and-reporting/sftp-event-file-configuration-tutorial.md part=0-end -->

# SFTP event file configuration tutorial

This guide steps you through using SFTP to retrieve Pismo batch event files. Pismo's SFTP service abstracts the S3 bucket behind an SFTP layer — when you connect, you access the same event files.

<Callout icon="📘" theme="info">
  You can associate up to **8 SSH keys** per organization. Sandbox and production credentials are separate.
</Callout>

Prerequisites:

* An SFTP client (FileZilla, WinSCP, or your own implementation)

* An SSH RSA key pair (we'll generate one below)

<Callout icon="⚠️" theme="warn">
  **File retention and download responsibility.** Pismo retains files on the SFTP server while your organization is active. However, we strongly recommend downloading files to your own infrastructure as soon as they are produced — either in real time (triggered by event notifications) or within 24 hours if you use a batch/polling strategy. These files belong to your organization, and keeping a local copy ensures you always have access. Please note that Pismo may charge additional fees for recovery requests of files older than 30 days.
</Callout>

## Step 1: Generate an SSH RSA Key Pair

You need an **RSA** key pair. The public key goes to Pismo; the private key stays with you.

### Option A: Command Line (Linux / macOS / Windows with Git Bash)

```
# Generate a 4096-bit RSA key pair
ssh-keygen -t rsa -b 4096 -C "pismo-sftp" -f ~/.ssh/pismo_sftp_rsa

# When prompted for a passphrase, press Enter for no passphrase
# (or set one if your security policy requires it)

# View the public key (this is what you send to Pismo)
cat ~/.ssh/pismo_sftp_rsa.pub
```

The output looks like:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDx... pismo-sftp
```

<Callout icon="📘" theme="info">
  **Important:** Use -t rsa. Other key types (ed25519, ecdsa) are not supported by Pismo's SFTP service.
</Callout>

### Option B: PuTTYgen (Windows GUI)

1. Download and open **PuTTYgen** (included with PuTTY: <Anchor label="https://www.putty.org" target="_blank" href="https://www.putty.org">[https://www.putty.org](https://www.putty.org)</Anchor>).
2. In **Type of key to generate**, select **RSA**.
3. Set **Number of bits** to **4096**.
4. Click **Generate** and move the mouse to create randomness.
5. Save the **private key** (`.ppk` file) to a secure location.
6. Copy the **public key** text from the top box (starts with `ssh-rsa`).
7. Use **Conversions > Export OpenSSH** key if you need the key in OpenSSH format for CLI tools.

## Step 2: Open a Service Desk Ticket

1. Go to: [https://pismolabs.atlassian.net/servicedesk/customer/portal/10](https://pismolabs.atlassian.net/servicedesk/customer/portal/10)
2. Click **Settings**
3. In **Category**, select **Data**   .
4. Enter a short description of the incident you are reporting in the **Summary** field.
5. In **Sub-Category**, select **File Integration**.
6. Copy the template below into the **Description** field, fill in your values, and submit:

```
INTEGRATION REQUEST — SFTP (Batch File Delivery)
=================================================

Org ID:          TN-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Environment:     Production / Sandbox
Requester Name:  Your Name
Contact Email:   you@company.com

SSH Public Key(s):
  (paste one per line, each starting with ssh-rsa)
  ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ...

IP Addresses (CIDR /32 — one per line):
  203.0.113.10/32
  198.51.100.20/32
```

7. When a Control Center request fails, the application automatically displays a popup message. You can add this message in the **Report Log** field.
8. In **Priority**, select a priority level.
9. In **Environment**, select the environment for which you want the configuration.
10. Click **Send** to submit the request.

<Callout icon="⏱️" theme="default">
  **Important:** After Pismo completes the initial configuration, you have **24 hours** to adjust permissions/access on your side. If Pismo cannot deliver events within this window, the integration will be paused and you will need to open a new ticket to resume.
</Callout>

### CLI: Find your public IP to include in the template:

```
curl -s ifconfig.me && echo "/32"
```

<Callout icon="📘" theme="info">
  Only the listed IP addresses will be allowed to connect. Use /32 subnet mask (single IP). You can attach the public key as a file instead of pasting it.
</Callout>

<Callout icon="⚠️" theme="warn">
  **IP limit:** A maximum of **5 IP addresses per organization** is allowed to limit the exposure surface of the environment.
</Callout>

## Step 3: Connect

After Pismo processes your ticket, you'll receive your SFTP username. Configure your client using the following information:

| Environment                       | Endpoint                         | Port |
| --------------------------------- | -------------------------------- | ---- |
| Sandbox / Development             | sftp-main.data.pismolabs.io      | 22   |
| Production Multi Tenant Brazil    | sftp-main.data.pismo.io          | 22   |
| Production Multi Tenant India     | sftp-main.data.ind.pismo.io      | 22   |
| Production Multi Tenant USA       | sftp-main.data.usa.pismo.io      | 22   |
| Production Multi Tenant Australia | sftp-main.data.aus.pismo.io      | 22   |
| Production Multi Tenant Indonesia | sftp-main.data.idn-prod.pismo.io | 22   |
| Production Multi Tenant Ireland   | sftp-main.data.irl.pismo.io      | 22   |
| Production Multi Tenant Brazil 02 | sftp-main.data.bra02.pismo.io    | 22   |

### CLI connection:

Use the following to establish your CLI connection.

```
# Connect using your private key (replace values)
sftp -i ~/.ssh/pismo_sftp_rsa -P 22 YOUR_USERNAME@sftp-main.data.pismolabs.io

# Once connected, list available files
ls /main_stream/

# Download a specific file
get /main_stream/FILENAME ./local-download/
```

### GUI connection (FileZilla):

1. Open **Site Manager > New Site**.

2. Protocol: **SFTP**.

3. Host: `sftp-main.data.pismolabs.io` (or `sftp-main.data.pismo.io` for prod)   .

4. For Port, use `22   `.

5. For **Logon Type**, select **Key file**.

6. User: Enter your username from Pismo   .

7. Key file: Enter your path to your private key   .

8. Click **Connect**.

## Step 4: Download Files

```
# Batch download all files from main_stream
sftp -i ~/.ssh/pismo_sftp_rsa YOUR_USERNAME@sftp-main.data.pismolabs.io <<EOF
cd /main_stream
lcd ./downloads
mget *
bye
EOF
```

## Knowing When Files Are Available

You can optionally set up real-time event notifications through a cloud account to be notified when new files arrive. Otherwise, periodically connect and check for new files in the `/main_stream/` directory (for example, daily or hourly polling).

<Callout icon="📘" theme="info">
  **Need Pismo-specific details?** Information such as Pismo's AWS Account ID, single-tenant SFTP endpoints, consumer role ARNs, or external IDs can be obtained from your **Technical Account Manager (TAM)** or the **Implementation Engineer** assigned to your project.
</Callout>

## Validate Integration

Run this diagnostic script to validate your integration. It checks all configuration steps and provides troubleshooting guidance:

````
#!/bin/bash
# ============================================================
#  SFTP Troubleshooting — Pismo Data Platform
# ============================================================
SFTP_USER="your-username"                        # ← replace
SFTP_HOST="sftp-main.data.pismolabs.io"          # ← replace for prod
SFTP_KEY="$HOME/.ssh/pismo_sftp_rsa"             # ← replace
SFTP_PORT=22
PASS=0; FAIL=0

echo "============================================================"
echo "  SFTP Integration Diagnostics"
echo "============================================================"

# 1. Private key exists?
echo "[1/7] Checking private key file..."
if [ -f "$SFTP_KEY" ]; then
    echo "  ✅ PASS — Found: $SFTP_KEY"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Not found: $SFTP_KEY"
    echo "  → Fix: ssh-keygen -t rsa -b 4096 -C pismo-sftp -f $SFTP_KEY"
    FAIL=$((FAIL+1))
fi

# 2. Key is RSA?
echo "[2/7] Verifying key type..."
KEY_INFO=$(ssh-keygen -l -f "$SFTP_KEY" 2>/dev/null)
if echo "$KEY_INFO" | grep -q "(RSA)"; then
    echo "  ✅ PASS — Key is RSA"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Key is NOT RSA: $KEY_INFO"
    echo "  → Pismo SFTP only supports RSA. Regenerate the key."
    FAIL=$((FAIL+1))
fi

# 3. Key permissions?
echo "[3/7] Checking permissions..."
if [ "$(stat -f '%A' "$SFTP_KEY" 2>/dev/null || stat -c '%a' "$SFTP_KEY" 2>/dev/null)" = "600" ]; then
    echo "  ✅ PASS — Permissions are 600"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Wrong permissions (should be 600)"
    echo "  → Fix: chmod 600 $SFTP_KEY"
    FAIL=$((FAIL+1))
fi

# 4. DNS resolves?
echo "[4/7] Resolving $SFTP_HOST..."
if host "$SFTP_HOST" >/dev/null 2>&1; then
    echo "  ✅ PASS — DNS resolves"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Cannot resolve hostname"
    echo "  → Check DNS or network connectivity"
    FAIL=$((FAIL+1))
fi

# 5. TCP port reachable?
echo "[5/7] Testing TCP to $SFTP_HOST:$SFTP_PORT..."
if nc -z -w 5 "$SFTP_HOST" "$SFTP_PORT" 2>/dev/null; then
    echo "  ✅ PASS — Port $SFTP_PORT reachable"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Port $SFTP_PORT unreachable"
    echo "  → Your IP may not be whitelisted"
    echo "  → Your public IP: $(curl -s ifconfig.me 2>/dev/null)"
    echo "  → Check firewall/VPN allows outbound port $SFTP_PORT"
    FAIL=$((FAIL+1))
fi

# 6. SSH auth works?
echo "[6/7] Testing SSH authentication..."
SSH_OUT=$(ssh -i "$SFTP_KEY" -p "$SFTP_PORT" -o BatchMode=yes \
    -o ConnectTimeout=10 -o StrictHostKeyChecking=no \
    "$SFTP_USER@$SFTP_HOST" "exit" 2>&1)
if [ $? -eq 0 ] || echo "$SSH_OUT" | grep -qi "subsystem"; then
    echo "  ✅ PASS — Authentication succeeded"
    PASS=$((PASS+1))
elif echo "$SSH_OUT" | grep -qi "permission denied"; then
    echo "  ❌ FAIL — Permission denied"
    echo "  → Public key mismatch. Verify key fingerprint:"
    echo "    ssh-keygen -l -f $SFTP_KEY"
    FAIL=$((FAIL+1))
else
    echo "  ❌ FAIL — $SSH_OUT"
    FAIL=$((FAIL+1))
fi

# 7. File listing works?
echo "[7/7] Testing SFTP file listing..."
SFTP_OUT=$(echo "ls /main_stream/" | sftp -i "$SFTP_KEY" -P "$SFTP_PORT" \
    -o ConnectTimeout=10 -o BatchMode=yes "$SFTP_USER@$SFTP_HOST" 2>&1)
if [ $? -eq 0 ]; then
    echo "  ✅ PASS — Can list /main_stream/"
    PASS=$((PASS+1))
else
    echo "  ❌ FAIL — Cannot list files"
    echo "  → $SFTP_OUT"
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
    echo "Integration Type: SFTP File Delivery"
    echo ""
    echo "=== CONFIGURATION ==="
    echo "SFTP Host: $SFTP_HOST"
    echo "SFTP User: $SFTP_USER"
    echo "SSH Key File: $SFTP_KEY"
    echo ""
    echo "=== TEST RESULTS ==="
    echo "Passed: $PASS"
    echo "Failed: $FAIL"
    echo ""
    echo "=== SSH KEY FINGERPRINT ==="
    ssh-keygen -lf "$SFTP_KEY" 2>/dev/null || echo "Could not retrieve"
    echo ""
    echo "=== PUBLIC KEY (for verification) ==="
    cat "${SFTP_KEY}.pub" 2>/dev/null || ssh-keygen -y -f "$SFTP_KEY" 2>/dev/null || echo "Could not retrieve"
    echo ""
    echo "=== SFTP HOST KEY ==="
    ssh-keyscan -p "$SFTP_PORT" "$SFTP_HOST" 2>/dev/null | head -3 || echo "Could not retrieve"
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
    echo "    • SFTP Gateway sync (S3-to-SFTP bridge)"
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
echo "  │  ⚠️  DO NOT share your private key — only the public key"
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

- `docs/data-and-reporting/sftp-event-file-configuration-tutorial.md`: updatedAt 2026-07-20T19:15:35.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/sftp-event-file-configuration-tutorial.md` | whole document | https://developers.pismo.io/pismo-docs/docs/sftp-event-file-configuration-tutorial | `189c63f664fbd2e2…` | 2026-07-20T19:15:35.000Z |

## Related knowledge units

- None.
