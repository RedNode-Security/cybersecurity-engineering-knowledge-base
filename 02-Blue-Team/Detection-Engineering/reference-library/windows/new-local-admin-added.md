---
title: New Local Administrator Added
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# New Local Administrator Added

## Detection ID

```text
DET-WINDOWS-NEW_LOCAL_ADMIN_ADDED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Privilege escalation may involve adding a user to local administrators.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `windows_security_events`

Required fields:

- `timestamp`
- `event_id`
- `actor`
- `target_user`
- `group`

## Normalized Logic

```text
event_id=4732 and group=Administrators and actor not approved
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-008",
  "windows_event_id": 4732,
  "actor": "EXAMPLE\\user",
  "target_user": "EXAMPLE\\temp",
  "group": "Administrators"
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-008",
  "windows_event_id": 4732,
  "actor": "EXAMPLE\\mdm-svc",
  "group": "Administrators",
  "approved_tool": true
}
```

## Expected False Positives

- MDM enrollment
- helpdesk support

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

Local admin changes on workstations are noisy unless joined with endpoint context.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-NEW_LOCAL_ADMIN_ADDED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
