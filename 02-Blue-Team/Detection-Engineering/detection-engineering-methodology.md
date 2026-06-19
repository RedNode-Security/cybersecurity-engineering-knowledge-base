---
title: Detection Engineering Methodology
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, siem, threat-hunting, engineering]
difficulty: intermediate
safe_publication: true
---


# Detection Engineering Methodology

## Overview

Detection engineering turns threat behavior into reliable, testable, and
maintainable detections. A detection is not only a query. It is an operational
artifact with a hypothesis, telemetry requirements, logic, false-positive model,
triage guidance, test plan, owner, review date, and success metrics.

## Lifecycle

```text
Threat Knowledge → Detection Hypothesis → Telemetry Mapping → Logic → Test → Deploy → Measure → Improve
```

## Step 1 — Define the Threat Behavior

Start with behavior, not tools or indicators.

Weak idea:

```text
Detect bad IPs.
```

Better idea:

```text
Detect a sequence where a user authenticates from a new source and performs a privileged action within 30 minutes.
```

Best idea:

```text
Detect likely account misuse by correlating unusual authentication context, privileged action, and lack of historical behavior for the account.
```

## Step 2 — Write the Hypothesis

Use a consistent structure:

```text
If <threat behavior> occurs, then <telemetry source> should show <observable pattern>.
```

Example:

```text
If password spraying succeeds, authentication logs may show many failed logons across many users from a shared source, followed by one or more successful logons.
```

## Step 3 — Map Telemetry

| Requirement | Example |
|---|---|
| Data source | Identity provider sign-in logs |
| Required fields | user, source IP, result, app, timestamp, MFA result |
| Join fields | user ID, device ID, source IP, session ID |
| Retention | At least 30 days for normal triage, longer for investigations |
| Blind spots | VPN egress hides original location; shared devices reduce confidence |

## Step 4 — Build Logic

Detection logic patterns:

| Pattern | Example | When useful |
|---|---|---|
| Threshold | 20 failures from one source in 10 minutes | Password attacks |
| Sequence | New login then admin action | Account misuse |
| Rare event | First time user assumes admin role | Privilege anomalies |
| Baseline | Host connects to new country | Behavioral changes |
| Indicator match | Domain in approved IOC list | Known campaigns |
| Policy violation | Root account used | Cloud governance |

## Step 5 — Validate Safely

Safe validation options:

- Lab event generation
- Vendor-provided test events
- Sanitized historical events
- Unit tests against sample logs
- Purple-team exercise under written authorization

Avoid validation that targets third-party systems or publishes exploit steps.

## Step 6 — Tune

Tuning should reduce noise without changing the original hypothesis. Document:

- Expected benign activity
- Allowlist criteria
- Suppression duration
- Business owner approval
- Risk accepted by tuning

## Step 7 — Triage Guidance

Every detection should include analyst steps:

1. Identify affected identity, host, and resource.
2. Review timeline before and after the alert.
3. Check whether activity matches approved business context.
4. Enrich with asset criticality and user role.
5. Look for related alerts or similar behavior.
6. Classify and escalate if suspicious.

## Example Detection Record

| Field | Value |
|---|---|
| Name | Unusual sign-in followed by privileged action |
| Hypothesis | Account misuse may show risky authentication followed by privileged change |
| Data sources | IdP sign-ins, admin audit logs, asset inventory |
| Severity | High if privileged group or sensitive asset involved |
| Confidence | Medium until enriched with baseline and change ticket context |
| False positives | Travel, new device, planned admin work, emergency access test |
| Triage | Review sign-in context, admin action, change ticket, endpoint health |
| Response | Revoke sessions, reset password, remove unauthorized privilege |

## Metrics

- Alert count per week
- True positive count
- False positive categories
- Mean time to triage
- Mean time to escalate
- Detections without owner
- Detections past review date

## References

- MITRE ATT&CK: https://attack.mitre.org/
- Sigma: https://sigmahq.io/
- Splunk Security Content: https://research.splunk.com/
