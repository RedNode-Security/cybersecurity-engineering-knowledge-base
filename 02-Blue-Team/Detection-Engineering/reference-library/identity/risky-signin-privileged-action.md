---
title: Risky Sign-in Followed by Privileged Action
domain: blue-team
category: detection-reference
status: draft
created: 2026-06-19
updated: 2026-06-19
tags: [detection, identity, reference]
difficulty: advanced
safe_publication: true
---


# Risky Sign-in Followed by Privileged Action

## Detection ID

```text
DET-IDENTITY-RISKY_SIGNIN_PRIVILEGED_ACTION
```

## Scope

This reference page documents a platform-neutral detection. It is intended for
defensive monitoring, triage, and detection engineering review. It is not a
copy-paste production rule; map the fields to your SIEM schema before deployment.

## Hypothesis

Account misuse may show risky authentication followed by privileged action.

## Why This Detection Exists

This detection covers a behavior that commonly appears during misuse, compromise,
misconfiguration, or control failure. The goal is to produce an alert with enough
context for an analyst to make a decision, not simply to match a string.

## Required Telemetry

Data sources: `identity_signin_logs`, `admin_audit_logs`

Required fields:

- `timestamp`
- `user`
- `source_ip`
- `risk`
- `action`

## Normalized Logic

```text
risky_signin(user) join privileged_action(user) within 60m
```

## Positive Sample Event

```json
{
  "event_id": "evt-id-002",
  "timestamp": "2026-06-19T10:20:00Z",
  "user": "admin@example.com",
  "risk": "high",
  "action": "Add member to privileged role",
  "minutes_since_signin": 12
}
```

## Benign or Expected Sample Event

```json
{
  "event_id": "evt-id-benign-002",
  "timestamp": "2026-06-19T10:20:00Z",
  "user": "admin@example.com",
  "risk": "low",
  "action": "Approved role activation",
  "change_id": "CHG-100"
}
```

## Expected False Positives

- approved admin change
- travel with managed device

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

The join matters. A risky sign-in without impact is different from a risky sign-in followed by privilege.

## Tuning Guidance

Tune with business context, not broad suppression. Prefer adding enrichment such
as asset criticality, user role, known automation, change windows, and owner
metadata. If a detection is noisy, record the false-positive category before
changing thresholds.

## Test Case

```text
TEST-DET-IDENTITY-RISKY_SIGNIN_PRIVILEGED_ACTION
```

Use the positive and benign sample events in the domain dataset to validate the
logic before writing a SIEM-specific query.

## Maintenance

- Owner: detection-engineering
- Review cadence: quarterly
- Review trigger: parser change, log-source change, incident feedback, or alert volume change
