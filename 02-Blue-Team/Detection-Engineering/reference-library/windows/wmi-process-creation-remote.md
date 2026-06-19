---
title: Remote WMI Process Creation
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# Remote WMI Process Creation

## Detection ID

```text
DET-WINDOWS-WMI_PROCESS_CREATION_REMOTE
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Lateral movement may use remote WMI process creation.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `edr_process_events`, `windows_security_events`

Required fields:

- `timestamp`
- `host`
- `source_host`
- `process`
- `parent_process`

## Normalized Logic

```text
parent_process=wmiprvse.exe and source_host not admin_jump_hosts
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-010",
  "host": "server01",
  "source_host": "workstation44",
  "parent_process": "wmiprvse.exe",
  "process": "cmd.exe"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-010",
  "host": "server01",
  "source_host": "adminjump01",
  "parent_process": "wmiprvse.exe",
  "approved_admin": true
}
```

## Expected False Positives

- endpoint management
- admin automation

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

Remote admin tools are legitimate. The source host and user matter.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-WMI_PROCESS_CREATION_REMOTE
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
