---
title: Authorized Keys Modified
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, linux, reference]
difficulty: advanced
safe_publication: true
---


# Authorized Keys Modified

## Detection ID

```text
DET-LINUX-AUTHORIZED_KEYS_MODIFIED
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Persistence may involve adding SSH authorized keys.

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
authorized_keys modified and no change context
```

## Positive Sample Event

```json
{
  "event_id": "evt-linux-003",
  "host": "linux01",
  "user": "deploy",
  "file_path": "/home/deploy/.ssh/authorized_keys",
  "new_key": true
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-linux-benign-003",
  "host": "linux01",
  "user": "deploy",
  "change_id": "CHG-6",
  "new_key": true
}
```

## Expected False Positives

- approved key rotation

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

Key changes are high-signal on sensitive servers.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-LINUX-AUTHORIZED_KEYS_MODIFIED
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
