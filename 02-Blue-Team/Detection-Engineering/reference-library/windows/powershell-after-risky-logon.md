---
title: PowerShell After Risky Logon
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# PowerShell After Risky Logon

## Detection ID

```text
DET-WINDOWS-POWERSHELL_AFTER_RISKY_LOGON
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Compromised users may execute scripts after risky authentication.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_signin_logs`, `edr_process_events`

Required fields:

- `timestamp`
- `user`
- `process`
- `command_line`

## Normalized Logic

```text
risky_signin join powershell_execution within 4h
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-003",
  "user": "user@example.com",
  "process": "powershell.exe",
  "risky_signin_1h": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-003",
  "user": "admin@example.com",
  "process": "powershell.exe",
  "change_id": "CHG-2"
}
```

## Expected False Positives

- admin maintenance

## Triage Workflow

1. Confirm affected entity and timestamp
2. Review surrounding events for 24 hours
3. Check approved change or expected business activity
4. Escalate if behavior remains unexplained

## Response Guidance

- Preserve relevant logs
- Open an incident case if suspicious
- Contain affected identity, host, or resource if compromise is confirmed

## Analyst Note

PowerShell is not bad by itself. Parent process and user context decide the case.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-POWERSHELL_AFTER_RISKY_LOGON
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
