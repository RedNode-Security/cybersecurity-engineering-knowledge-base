---
title: Scheduled Task Created by Unusual User
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, windows, reference]
difficulty: advanced
safe_publication: true
---


# Scheduled Task Created by Unusual User

## Detection ID

```text
DET-WINDOWS-SCHEDULED_TASK_UNUSUAL_USER
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Persistence may involve scheduled task creation by unusual users.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `windows_task_scheduler`, `edr_process_events`

Required fields:

- `timestamp`
- `host`
- `user`
- `task_name`

## Normalized Logic

```text
scheduled_task_created and user rare_for_task_creation
```

## Positive Sample Event

```json
{
  "event_id": "evt-win-005",
  "host": "workstation01",
  "user": "EXAMPLE\\user",
  "task_name": "Updater",
  "rare_for_user": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-win-benign-005",
  "host": "workstation01",
  "user": "EXAMPLE\\admin",
  "task_name": "ApprovedMaintenance",
  "change_id": "CHG-4"
}
```

## Expected False Positives

- IT automation

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

The task action command is often the most important field.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-WINDOWS-SCHEDULED_TASK_UNUSUAL_USER
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
