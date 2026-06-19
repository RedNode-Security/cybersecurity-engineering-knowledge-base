---
title: Office Spawns Script Interpreter
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# Office Spawns Script Interpreter

## Detection ID

```text
DET-WINDOWS-OFFICE_SPAWNS_SCRIPT_INTERPRETER
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Phishing execution may involve Office spawning script interpreters.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `edr_process_events`

Required fields:

- `timestamp`
- `host`
- `parent_process`
- `process`
- `command_line`

## Normalized Logic

```text
parent in office_apps and child in script_interpreters
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-007",
  "parent_process": "winword.exe",
  "process": "powershell.exe",
  "network_connection": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-007",
  "parent_process": "excel.exe",
  "process": "powershell.exe",
  "approved_macro": true
}
```

## Expected False Positives

- approved macro automation

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

This is strongest when paired with email delivery or external document open.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-OFFICE_SPAWNS_SCRIPT_INTERPRETER
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
