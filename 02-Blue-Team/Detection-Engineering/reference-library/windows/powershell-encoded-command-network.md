---
title: PowerShell Encoded Command With Network
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# PowerShell Encoded Command With Network

## Detection ID

```text
DET-WINDOWS-POWERSHELL_ENCODED_COMMAND_NETWORK
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Suspicious script execution may use encoded command and network access.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `edr_process_events`

Required fields:

- `timestamp`
- `host`
- `process`
- `command_line`
- `network_connection`

## Normalized Logic

```text
powershell encoded_command and network_connection and not approved_tool
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-012",
  "process": "powershell.exe",
  "encoded_command": true,
  "network_connection": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-012",
  "process": "powershell.exe",
  "encoded_command": true,
  "management_tool": true
}
```

## Expected False Positives

- endpoint management

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

Encoded command is a signal, not a verdict. Pair it with parent and network behavior.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-POWERSHELL_ENCODED_COMMAND_NETWORK
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
