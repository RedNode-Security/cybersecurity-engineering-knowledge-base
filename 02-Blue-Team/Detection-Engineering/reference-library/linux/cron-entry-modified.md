---
title: Cron Entry Modified by Unusual User
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, linux, reference]
difficulty: advanced
safe_publication: true
---


# Cron Entry Modified by Unusual User

## Detection ID

```text
DET-LINUX-CRON_ENTRY_MODIFIED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Persistence may involve cron modifications.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `linux_audit_logs`, `edr_file_events`

Required fields:

- `timestamp`
- `host`
- `user`
- `file_path`

## Normalized Logic

```text
cron_path modified by unusual user
```

## Positive Sample Event

```json
{
  "event_id": "evt-linux-005",
  "user": "www-data",
  "file_path": "/var/spool/cron/www-data",
  "new_entry": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-linux-benign-005",
  "user": "root",
  "file_path": "/etc/cron.d/backup",
  "change_id": "CHG-8"
}
```

## Expected False Positives

- scheduled maintenance

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

Cron entries from service users are more suspicious than root-managed cron in a change window.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-LINUX-CRON_ENTRY_MODIFIED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
